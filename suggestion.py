def generate_health_advice(bmi, whr, whtr, bfp, waist_cm, gender, arm_to_leg_ratio):
    """Generate personalized health advice based on body composition metrics"""
    
    advice = []
    
    # BMI-based advice with detailed recommendations
    if bmi < 18.5:
        advice.append({
            "category": "💪 Weight & Health Advice Summary",
            "title": "Your weight category is Underweight.",
            "suggestions": [
                "Consider consulting a health expert for personalized guidance.",
                "Focus on healthy weight gain through balanced nutrition:",
                "  • Aim for 5-6 small meals throughout the day",
                "  • Include protein-rich foods (lean meats, fish, eggs, legumes)",
                "  • Add healthy fats (avocados, nuts, olive oil)",
                "  • Include complex carbohydrates (whole grains, sweet potatoes)",
                "  • Consider protein shakes between meals",
                "• Strength training recommendations:",
                "  • Focus on compound exercises (squats, deadlifts, bench press)",
                "  • Start with 2-3 sessions per week",
                "  • Gradually increase weights and intensity",
                "• Monitor progress:",
                "  • Track weight weekly",
                "  • Keep a food diary",
                "  • Record workout progress"
            ]
        })
    elif 18.5 <= bmi < 25:
        advice.append({
            "category": "💪 Weight & Health Advice Summary",
            "title": "Your weight category is Normal.",
            "suggestions": [
                "Maintain your current healthy lifestyle with these recommendations:",
                "• Nutrition:",
                "  • Follow a balanced diet with all food groups",
                "  • Stay hydrated (2-3 liters of water daily)",
                "  • Include variety of fruits and vegetables",
                "  • Choose whole grains over refined grains",
                "• Physical Activity:",
                "  • 150 minutes of moderate exercise weekly",
                "  • Mix cardio and strength training",
                "  • Include flexibility exercises",
                "• Lifestyle:",
                "  • Get 7-9 hours of sleep",
                "  • Manage stress through meditation or yoga",
                "  • Regular health check-ups",
                "• Maintenance Tips:",
                "  • Track measurements monthly",
                "  • Adjust diet based on activity level",
                "  • Stay consistent with exercise routine"
            ]
        })
    elif 25 <= bmi < 30:
        advice.append({
            "category": "💪 Weight & Health Advice Summary",
            "title": "Your weight category is Overweight.",
            "suggestions": [
                "Consider consulting a health expert for personalized guidance.",
                "Weight Management Plan:",
                "• Nutrition Strategy:",
                "  • Create a moderate calorie deficit (500-750 calories)",
                "  • Focus on protein (1.6-2.2g per kg of body weight)",
                "  • Include fiber-rich foods",
                "  • Limit processed foods and added sugars",
                "  • Practice portion control",
                "• Exercise Plan:",
                "  • Start with 30 minutes of cardio 3-4 times weekly",
                "  • Include strength training 2-3 times weekly",
                "  • Gradually increase intensity",
                "  • Add daily movement (walking, stairs)",
                "• Progress Tracking:",
                "  • Weekly weight measurements",
                "  • Monthly body measurements",
                "  • Food diary",
                "  • Exercise log",
                "• Support System:",
                "  • Join a weight loss group",
                "  • Find an accountability partner",
                "  • Consider working with a nutritionist"
            ]
        })
    else:
        advice.append({
            "category": "💪 Weight & Health Advice Summary",
            "title": "Your weight category is Obese.",
            "suggestions": [
                "Consider consulting a health expert for personalized guidance.",
                "Comprehensive Health Management Plan:",
                "• Medical Consultation:",
                "  • Regular check-ups for blood pressure, sugar, and cholesterol",
                "  • Discuss weight loss medications if appropriate",
                "  • Monitor for obesity-related conditions",
                "• Nutrition Plan:",
                "  • Work with a registered dietitian",
                "  • Focus on whole, unprocessed foods",
                "  • Create sustainable eating habits",
                "  • Learn proper portion control",
                "• Exercise Strategy:",
                "  • Start with low-impact activities (walking, swimming)",
                "  • Gradually increase duration and intensity",
                "  • Include strength training for muscle preservation",
                "  • Consider working with a personal trainer",
                "• Lifestyle Modifications:",
                "  • Improve sleep quality",
                "  • Stress management techniques",
                "  • Reduce sedentary time",
                "  • Build a support network",
                "• Progress Monitoring:",
                "  • Weekly weight tracking",
                "  • Monthly measurements",
                "  • Regular health check-ups",
                "  • Food and exercise journal"
            ]
        })
    
    # WHtR-based advice with detailed recommendations
    if whtr > 0.5:
        advice.append({
            "category": "🚨 Waist-to-Height Ratio Warning",
            "title": "Waist-to-height ratio exceeds 0.5, indicating abdominal fat risk.",
            "suggestions": [
                "Central Obesity Management Plan:",
                "• Dietary Modifications:",
                "  • Reduce processed carbohydrates",
                "  • Increase fiber intake (25-30g daily)",
                "  • Choose whole grains over refined grains",
                "  • Include lean proteins",
                "  • Add healthy fats (omega-3s)",
                "• Exercise Focus:",
                "  • Core-strengthening exercises",
                "  • High-intensity interval training",
                "  • Regular cardio exercise",
                "  • Posture improvement exercises",
                "• Lifestyle Changes:",
                "  • Stress management techniques",
                "  • Improve sleep quality",
                "  • Reduce alcohol consumption",
                "  • Quit smoking if applicable",
                "• Monitoring:",
                "  • Track waist measurements weekly",
                "  • Monitor blood pressure",
                "  • Regular blood sugar checks"
            ]
        })
    
    # WHR-based advice with detailed recommendations
    if (gender.upper() == 'M' and whr > 0.90) or (gender.upper() == 'F' and whr > 0.85):
        advice.append({
            "category": "⚠️ Waist-to-Hip Ratio Warning",
            "title": "High WHR: Increased risk of heart disease and type 2 diabetes.",
            "suggestions": [
                "Cardiovascular Health Management Plan:",
                "• Dietary Recommendations:",
                "  • Mediterranean-style diet",
                "  • Increase fiber intake",
                "  • Reduce saturated fats",
                "  • Include omega-3 rich foods",
                "  • Limit processed foods",
                "• Exercise Program:",
                "  • Regular cardiovascular exercise",
                "  • Strength training",
                "  • Flexibility exercises",
                "  • Stress-reducing activities",
                "• Health Monitoring:",
                "  • Regular blood pressure checks",
                "  • Lipid profile monitoring",
                "  • Blood sugar testing",
                "  • Track measurements monthly",
                "• Lifestyle Modifications:",
                "  • Stress management",
                "  • Adequate sleep",
                "  • Regular physical activity",
                "  • Smoking cessation if applicable"
            ]
        })
    
    # Arm-to-Leg ratio advice with detailed recommendations
    if arm_to_leg_ratio > 1.1:
        advice.append({
            "category": "🧍 Body Proportion Advice",
            "title": "High arm-to-leg ratio — consider balancing workouts for both lower and upper body.",
            "suggestions": [
                "Balanced Strength Training Plan:",
                "• Lower Body Focus:",
                "  • Squats (3 sets, 10-12 reps)",
                "  • Lunges (3 sets, 10-12 reps each leg)",
                "  • Leg presses (3 sets, 10-12 reps)",
                "  • Calf raises (3 sets, 15-20 reps)",
                "• Cardio Options:",
                "  • Cycling",
                "  • Swimming",
                "  • Stair climbing",
                "• Training Schedule:",
                "  • 3-4 sessions per week",
                "  • Alternate upper and lower body days",
                "  • Include rest days",
                "• Progress Tracking:",
                "  • Record workout progress",
                "  • Take measurements monthly",
                "  • Track strength improvements"
            ]
        })
    elif arm_to_leg_ratio < 0.9:
        advice.append({
            "category": "🧍 Body Proportion Advice",
            "title": "Low arm-to-leg ratio — consider strengthening upper body.",
            "suggestions": [
                "Upper Body Strength Development Plan:",
                "• Upper Body Exercises:",
                "  • Push-ups (3 sets, 10-15 reps)",
                "  • Pull-ups (3 sets, 8-12 reps)",
                "  • Dumbbell rows (3 sets, 10-12 reps)",
                "  • Shoulder presses (3 sets, 10-12 reps)",
                "• Training Schedule:",
                "  • 3-4 sessions per week",
                "  • Focus on compound movements",
                "  • Include rest days",
                "• Progress Tracking:",
                "  • Record workout progress",
                "  • Take measurements monthly",
                "  • Track strength improvements"
            ]
        })
    
    # General wellness tips with detailed recommendations
    advice.append({
        "category": "🌿 General Wellness Tips",
        "title": "Maintain overall health and well-being",
        "suggestions": [
            "Comprehensive Wellness Plan:",
            "• Sleep Optimization:",
            "  • Maintain 7-9 hours of quality sleep",
            "  • Establish regular sleep schedule",
            "  • Create sleep-friendly environment",
            "  • Limit screen time before bed",
            "• Stress Management:",
            "  • Daily meditation practice",
            "  • Regular exercise",
            "  • Nature walks",
            "  • Journaling",
            "• Hydration:",
            "  • Drink 2-3 liters of water daily",
            "  • Limit caffeine and alcohol",
            "  • Monitor urine color",
            "• Nutrition:",
            "  • Regular meal timing",
            "  • Balanced macronutrients",
            "  • Adequate protein intake",
            "  • Vitamin and mineral-rich foods",
            "• Physical Activity:",
            "  • Daily movement",
            "  • Regular exercise",
            "  • Posture awareness",
            "  • Stretching routine"
        ]
    })
    
    # Analysis summary with detailed explanation
    advice.append({
        "category": "--- Analysis Summary ---",
        "title": "Health Indicators Analysis",
        "suggestions": [
            "Comprehensive Health Assessment:",
            "• Body Composition Analysis:",
            "  • BMI indicates weight category",
            "  • Body fat percentage shows fat distribution",
            "  • Muscle mass indicates strength potential",
            "• Risk Factor Assessment:",
            "  • WHR indicates abdominal fat distribution",
            "  • WHtR shows central obesity risk",
            "  • Metabolic risk factors identified",
            "• Progress Tracking:",
            "  • Regular measurements recommended",
            "  • Track changes over time",
            "  • Adjust plan based on progress",
            "• Next Steps:",
            "  • Follow recommended exercise plan",
            "  • Implement dietary changes",
            "  • Monitor progress regularly",
            "  • Consult healthcare provider as needed"
        ]
    })
    
    return advice

def print_health_advice(advice_list):
    """Print the health advice in a formatted way"""
    for advice in advice_list:
        print(f"\n{advice['category']}")
        print(advice['title'])
        for suggestion in advice['suggestions']:
            print(f"→ {suggestion}")

if __name__ == "__main__":
    # Example usage
    from BMI_calc import get_body_composition_summary, load_current_user
    
    try:
        current_user_id = load_current_user()
        if current_user_id is None:
            print("❌ Please log in first to get health advice.")
            print("Run 'python Login_page.py' to log in.")
        else:
            # Get user data and calculate metrics
            from BMI_calc import get_user_data, calculate_age
            user_data = get_user_data(current_user_id)
            
            # Calculate age
            age = calculate_age(user_data['date_of_birth'])
            
            # Get measurements
            weight_kg = user_data['weight']
            height_cm = user_data['height']
            height_m = height_cm / 100
            gender = user_data['gender']
            waist_cm = user_data['waist']
            hip_cm = user_data['hip']
            arm_length_cm = user_data['arm_length']
            leg_length_cm = user_data['leg_length']
            
            # Calculate metrics
            bmi = weight_kg / (height_m ** 2)
            whr = waist_cm / hip_cm
            whtr = waist_cm / height_cm
            bfp = (1.20 * bmi) + (0.23 * age) - (16.2 if gender.upper() == 'M' else 5.4)
            arm_to_leg_ratio = arm_length_cm / leg_length_cm
            
            # Generate and print advice
            advice = generate_health_advice(bmi, whr, whtr, bfp, waist_cm, gender, arm_to_leg_ratio)
            print_health_advice(advice)
            
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}") 