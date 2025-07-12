# from flask import Flask, request, jsonify
# from final__uni_recommendation_system import load_and_preprocess, get_top_matches

# app = Flask(__name__)

# # Load and preprocess data once when the API starts
# file_path = "university_dataset_real_2000 final.xlsx"
# df, df_encoded, ohe, cat_cols = load_and_preprocess(file_path)

# # API endpoint to get recommendations
# @app.route('/recommend', methods=['POST'])
# def recommend():
#     try:
#         # Get user input from request body
#         user_input = request.json
        
#         # Call the function to get the top matches
#         recommendations = get_top_matches(user_input, df, df_encoded, ohe, cat_cols)
        
#         return jsonify({'status': 'success', 'recommendations': recommendations}), 200
#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
from final__uni_recommendation_system import load_and_preprocess, get_top_matches

app = Flask(__name__)

# Load and preprocess data once when the API starts
file_path = "university_dataset_real_2000 final.xlsx"
df, df_encoded, ohe, cat_cols = load_and_preprocess(file_path)

# Set default values for optional fields
DEFAULT_VALUES = {
    "Country": "None",
    "City": "None",
    "Public_or_Private": "None",
    "Language_of_Instruction": "None",
    "Intake_Months": "None",
    "Mode_of_Study": "None",
    "Internship_Opportunities": "None"
}

# API endpoint to get recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Get user input from request body
        user_input = request.json

        # Ensure required fields exist
        required_fields = [
            "Field_Specialization", "Degree_Level", "Average_GPA_Requirement",
            "IELTS_Requirement", "Tuition_Fee_USD", "Living_Cost_Per_Year_USD",
            "Scholarship_Available", "Region"
        ]

        # Check if required fields are present
        for field in required_fields:
            if field not in user_input:
                return jsonify({'status': 'error', 'message': f'Missing required field: {field}'}), 400

        # For optional fields, set default values if not provided
        for field, default_value in DEFAULT_VALUES.items():
            if field not in user_input:
                user_input[field] = default_value

        # Call the function to get the top matches
        recommendations = get_top_matches(user_input, df, df_encoded, ohe, cat_cols)
        
        return jsonify({'status': 'success', 'recommendations': recommendations}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
