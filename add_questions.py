# all_questions = []

# # --- Sine ---
# sin = [
#     # Easy
#     {"topic": "Sine", "level": "easy", "question": "In a right triangle, sinθ equals:", 
#      "options": ["opposite/adjacent", "adjacent/hypotenuse", "opposite/hypotenuse", "hypotenuse/opposite"], 
#      "answer": "opposite/hypotenuse"},
#     {"topic": "Sine", "level": "easy", "question": "What is sin30°?", 
#      "options": ["0", "0.5", "√3/2", "1"], "answer": "0.5"},
#     {"topic": "Sine", "level": "easy", "question": "If opposite side = 4 and hypotenuse = 8, sinθ = ?", 
#      "options": ["0.25", "0.5", "0.75", "1"], "answer": "0.5"},
#     # Medium
#     {"topic": "Sine", "level": "medium", "question": "What is sin150°?", 
#      "options": ["0.5", "-0.5", "√3/2", "-√3/2"], "answer": "0.5"},
#     {"topic": "Sine", "level": "medium", "question": "In which quadrant is sine positive and cosine negative?", 
#      "options": ["I", "II", "III", "IV"], "answer": "II"},
#     # Hard
#     {"topic": "Sine", "level": "hard", "question": "Using sine addition formula, sin(A+B) = ?", 
#      "options": ["sinAcosB + cosAsinB", "sinAcosB - cosAsinB", "cosAcosB - sinAsinB", "cosAcosB + sinAsinB"], 
#      "answer": "sinAcosB + cosAsinB"}
# ]

# # --- Cosine ---
# cos = [
#     # Easy
#     {"topic": "Cosine", "level": "easy", "question": "cosθ in right triangle is:", 
#      "options": ["opposite/adjacent", "adjacent/hypotenuse", "opposite/hypotenuse", "hypotenuse/adjacent"], 
#      "answer": "adjacent/hypotenuse"},
#     {"topic": "Cosine", "level": "easy", "question": "What is cos60°?", 
#      "options": ["0", "0.5", "√3/2", "1"], "answer": "0.5"},
#     {"topic": "Cosine", "level": "easy", "question": "If adjacent = 3 and hypotenuse = 5, cosθ = ?", 
#      "options": ["0.6", "0.8", "1.2", "1.6"], "answer": "0.6"},
#     # Medium
#     {"topic": "Cosine", "level": "medium", "question": "What is cos120°?", 
#      "options": ["0.5", "-0.5", "√3/2", "-√3/2"], "answer": "-0.5"},
#     {"topic": "Cosine", "level": "medium", "question": "Law of Cosines formula is:", 
#      "options": ["a² = b² + c²", "a² = b² + c² - 2bc", "a² = b² + c² - 2bc cosA", "a² = b² + c² + 2bc cosA"], 
#      "answer": "a² = b² + c² - 2bc cosA"},
#     # Hard
#     {"topic": "Cosine", "level": "hard", "question": "Find side c using Law of Cosines: a=5, b=7, angle C=60°", 
#      "options": ["√39", "6", "7", "8"], "answer": "√39"}
# ]

# # --- Tangent ---
# tan = [
#     # Easy
#     {"topic": "Tangent", "level": "easy", "question": "tanθ equals:", 
#      "options": ["sinθ/cosθ", "cosθ/sinθ", "1/sinθ", "1/cosθ"], "answer": "sinθ/cosθ"},
#     {"topic": "Tangent", "level": "easy", "question": "What is tan45°?", 
#      "options": ["0", "1", "√3", "undefined"], "answer": "1"},
#     {"topic": "Tangent", "level": "easy", "question": "If opposite=6 and adjacent=2, tanθ = ?", 
#      "options": ["1/3", "3", "4", "8"], "answer": "3"},
#     # Medium
#     {"topic": "Tangent", "level": "medium", "question": "What is the period of tangent function?", 
#      "options": ["90°", "180°", "270°", "360°"], "answer": "180°"},
#     {"topic": "Tangent", "level": "medium", "question": "In which quadrant is tangent positive?", 
#      "options": ["I only", "I and II", "I and III", "All quadrants"], "answer": "I and III"},
#     # Hard
#     {"topic": "Tangent", "level": "hard", "question": "Solve: tanx = √3 for 0° ≤ x < 360°", 
#      "options": ["30°", "60°", "60° and 240°", "30° and 210°"], "answer": "60° and 240°"}
# ]

# # --- Trigonometric Equations ---
# trig_equations = [
#     # Easy
#     {"topic": "Trigonometric Equations", "level": "easy", "question": "Solve: sinx = 0.5 (principal solution)", 
#      "options": ["30°", "45°", "60°", "90°"], "answer": "30°"},
#     {"topic": "Trigonometric Equations", "level": "easy", "question": "Solve: cosx = 1", 
#      "options": ["0°", "30°", "45°", "90°"], "answer": "0°"},
#     {"topic": "Trigonometric Equations", "level": "easy", "question": "Solve: tanx = 1", 
#      "options": ["30°", "45°", "60°", "90°"], "answer": "45°"},
#     # Medium
#     {"topic": "Trigonometric Equations", "level": "medium", "question": "Solve: 2sinx - 1 = 0", 
#      "options": ["30°", "30° and 150°", "60°", "60° and 120°"], "answer": "30° and 150°"},
#     {"topic": "Trigonometric Equations", "level": "medium", "question": "Solve: cos2x = 0.5", 
#      "options": ["30°", "60°", "30° and 150°", "30° and 330°"], "answer": "30° and 150°"},
#     # Hard
#     {"topic": "Trigonometric Equations", "level": "hard", "question": "Solve: 2sin²x - sinx - 1 = 0", 
#      "options": ["90°", "210°", "270°", "90° and 270°"], "answer": "270°"}
# ]

# # Combine all topics
# all_questions += sin + cos + tan + trig_equations


# # Insert into MongoDB
# from pymongo import MongoClient

# client = MongoClient("mongodb+srv://alasylkhh:admin@cluster0.6fmla.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# questions = client['questions']
# questions_geometry = questions['trigonometry']
# questions_geometry.insert_many(all_questions)

# print("✅ Successfully inserted 30 questions across 5 Geometry topics into MongoDB!")