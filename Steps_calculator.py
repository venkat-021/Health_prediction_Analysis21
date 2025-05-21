import tkinter as tk
from tkinter import ttk, messagebox
from BMI_calc import load_current_user, get_user_data, calculate_age

# --- Diet and BMI logic from user ---
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def recommend_diet(bmi_category, total_calories):
    if bmi_category == "Underweight":
        carb_percent, fat_percent, fiber_g = 0.60, 0.30, 25
    elif bmi_category == "Normal weight":
        carb_percent, fat_percent, fiber_g = 0.55, 0.25, 30
    elif bmi_category == "Overweight":
        carb_percent, fat_percent, fiber_g = 0.45, 0.25, 35
    else:  # Obese
        carb_percent, fat_percent, fiber_g = 0.40, 0.20, 40

    carbs_g = round((carb_percent * total_calories) / 4)
    fat_g = round((fat_percent * total_calories) / 9)

    return {
        "calories": total_calories,
        "carbs_g": carbs_g,
        "fat_g": fat_g,
        "fiber_g": fiber_g,
        "goal": {
            "Underweight": "Weight gain",
            "Normal weight": "Maintain weight",
            "Overweight": "Fat loss",
            "Obese": "Obesity control"
        }[bmi_category]
    }

def calculate_bmr(weight, height_cm, age, gender):
    if gender.lower() == "male" or gender.upper() == "M":
        return round(10 * weight + 6.25 * height_cm - 5 * age + 5)
    elif gender.lower() == "female" or gender.upper() == "F":
        return round(10 * weight + 6.25 * height_cm - 5 * age - 161)
    else:
        raise ValueError("Gender must be 'male' or 'female'.")

# --- GUI Application ---
class StepsCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steps & Diet Plan Calculator")
        self.root.geometry("600x650")
        self.user_id = load_current_user()
        if self.user_id is None:
            messagebox.showerror("Error", "No user logged in. Please log in first.")
            root.destroy()
            return
        self.user_data = get_user_data(self.user_id)
        self.create_widgets()

    def create_widgets(self):
        # User info
        user = self.user_data
        ttk.Label(self.root, text=f"User: {user['username']}", font=("Arial", 12, "bold")).pack(pady=5)
        ttk.Label(self.root, text=f"Gender: {user['gender']}").pack()
        ttk.Label(self.root, text=f"Date of Birth: {user['date_of_birth']}").pack()
        ttk.Label(self.root, text=f"Current Weight (kg): {user['weight']}").pack()
        ttk.Label(self.root, text=f"Height (cm): {user['height']}").pack()
        
        # Target weight
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)
        ttk.Label(frame, text="Target Weight (kg):").grid(row=0, column=0, sticky=tk.W)
        self.target_weight_var = tk.StringVar(value=str(user['weight'] - 2))
        ttk.Entry(frame, textvariable=self.target_weight_var, width=10).grid(row=0, column=1)
        
        # Days
        ttk.Label(frame, text="Days to reach target:").grid(row=1, column=0, sticky=tk.W)
        self.days_var = tk.StringVar(value="30")
        ttk.Entry(frame, textvariable=self.days_var, width=10).grid(row=1, column=1)
        
        # Custom calories
        ttk.Label(frame, text="Custom daily calories (optional):").grid(row=2, column=0, sticky=tk.W)
        self.custom_cal_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.custom_cal_var, width=10).grid(row=2, column=1)
        
        # Calculate button
        ttk.Button(self.root, text="Calculate Plan", command=self.calculate_plan).pack(pady=10)
        
        # Output
        self.output_text = tk.Text(self.root, height=25, width=70)
        self.output_text.pack(pady=10)

    def calculate_plan(self):
        try:
            weight = float(self.user_data['weight'])
            target_weight = float(self.target_weight_var.get())
            days = int(self.days_var.get())
            height_cm = float(self.user_data['height'])
            height = height_cm / 100
            name = self.user_data['username']
            gender = self.user_data['gender']
            # Calculate age from date_of_birth
            age = calculate_age(self.user_data['date_of_birth'])
            if self.custom_cal_var.get():
                total_calories = int(self.custom_cal_var.get())
            else:
                total_calories = 2000
        except Exception as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")
            return

        bmi = round(weight / (height ** 2), 2)
        bmi_cat = bmi_category(bmi)
        bmr = calculate_bmr(weight, height_cm, age, gender)
        diet = recommend_diet(bmi_cat, total_calories)

        # Weight plan
        weight_diff = weight - target_weight
        total_calories_to_burn = weight_diff * 7700 if weight_diff > 0 else 0
        daily_calorie_burn_goal = total_calories_to_burn / days if weight_diff > 0 else 0

        # Net calories to burn = (diet + deficit) - BMR
        net_calories_to_burn = max(0, (total_calories + daily_calorie_burn_goal) - bmr)
        steps_per_day = int(net_calories_to_burn / 0.04)

        # Output
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"\n📊 Health Plan for {name}\n")
        self.output_text.insert(tk.END, f"🎯 Target: From {weight} kg → {target_weight} kg in {days} days\n")
        self.output_text.insert(tk.END, f"⚖️ Current BMI: {bmi} ({bmi_cat})\n")
        self.output_text.insert(tk.END, f"🧬 Estimated BMR ({gender.title()}): {bmr} kcal/day\n")

        if weight_diff > 0:
            self.output_text.insert(tk.END, f"🔥 You need to burn: {total_calories_to_burn:.0f} kcal total\n")
            self.output_text.insert(tk.END, f"📅 Daily burn target (for weight loss): {daily_calorie_burn_goal:.0f} kcal\n")
        else:
            self.output_text.insert(tk.END, "✅ No weight loss targeted.\n")

        self.output_text.insert(tk.END, f"🚶 Steps required per day: {steps_per_day} steps (after subtracting BMR)\n")

        self.output_text.insert(tk.END, f"\n🥗 Suggested Diet Plan (Calories: {total_calories} kcal):\n")
        self.output_text.insert(tk.END, f"🍚 Carbs: {diet['carbs_g']}g\n")
        self.output_text.insert(tk.END, f"🥑 Fat: {diet['fat_g']}g\n")
        self.output_text.insert(tk.END, f"🌾 Fiber: {diet['fiber_g']}g\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = StepsCalculatorApp(root)
    root.mainloop()
