# all_questions = []

# # --- Angles ---
# angles = [
#     # Easy
#     {"topic": "Angles", "level": "easy", "question": "What is the measure of a right angle?", "options": ["45°", "90°", "180°", "360°"], "answer": "90°"},
#     {"topic": "Angles", "level": "easy", "question": "Two angles that add up to 180° are called:", "options": ["Complementary", "Supplementary", "Vertical", "Adjacent"], "answer": "Supplementary"},
#     {"topic": "Angles", "level": "easy", "question": "If two angles are vertical angles, they are:", "options": ["Complementary", "Supplementary", "Equal", "Adjacent"], "answer": "Equal"},
#     # Medium
#     {"topic": "Angles", "level": "medium", "question": "In a triangle, the sum of all interior angles is:", "options": ["90°", "180°", "270°", "360°"], "answer": "180°"},
#     {"topic": "Angles", "level": "medium", "question": "Find angle x if two supplementary angles are x and 110°", "options": ["60°", "70°", "80°", "90°"], "answer": "70°"},
#     # Hard
#     {"topic": "Angles", "level": "hard", "question": "In a pentagon, what is the sum of interior angles?", "options": ["360°", "540°", "720°", "900°"], "answer": "540°"}
# ]

# # --- Triangles ---
# triangles = [
#     # Easy
#     {"topic": "Triangles", "level": "easy", "question": "How many sides does a triangle have?", "options": ["2", "3", "4", "5"], "answer": "3"},
#     {"topic": "Triangles", "level": "easy", "question": "A triangle with all sides equal is:", "options": ["Scalene", "Isosceles", "Equilateral", "Right"], "answer": "Equilateral"},
#     {"topic": "Triangles", "level": "easy", "question": "In a right triangle, the longest side is called:", "options": ["Base", "Height", "Hypotenuse", "Diagonal"], "answer": "Hypotenuse"},
#     # Medium
#     {"topic": "Triangles", "level": "medium", "question": "In a right triangle with legs 3 and 4, hypotenuse is:", "options": ["5", "6", "7", "8"], "answer": "5"},
#     {"topic": "Triangles", "level": "medium", "question": "What triangle has angles 45°, 45°, 90°?", "options": ["Scalene", "Equilateral", "Isosceles Right", "Obtuse"], "answer": "Isosceles Right"},
#     # Hard
#     {"topic": "Triangles", "level": "hard", "question": "In ΔABC, angle A=30°, angle B=60°, this is a ______ triangle", "options": ["Acute", "Obtuse", "Right", "Equilateral"], "answer": "Right"}
# ]

# # --- Quadrilaterals ---
# quadrilaterals = [
#     # Easy
#     {"topic": "Quadrilaterals", "level": "easy", "question": "How many sides does a quadrilateral have?", "options": ["3", "4", "5", "6"], "answer": "4"},
#     {"topic": "Quadrilaterals", "level": "easy", "question": "A quadrilateral with all right angles is a:", "options": ["Rhombus", "Rectangle", "Trapezoid", "Parallelogram"], "answer": "Rectangle"},
#     {"topic": "Quadrilaterals", "level": "easy", "question": "All sides equal but angles not 90° - this is a:", "options": ["Square", "Rectangle", "Rhombus", "Trapezoid"], "answer": "Rhombus"},
#     # Medium
#     {"topic": "Quadrilaterals", "level": "medium", "question": "In a parallelogram, opposite angles are:", "options": ["Equal", "Supplementary", "Complementary", "90°"], "answer": "Equal"},
#     {"topic": "Quadrilaterals", "level": "medium", "question": "What quadrilateral has exactly one pair of parallel sides?", "options": ["Parallelogram", "Rhombus", "Trapezoid", "Kite"], "answer": "Trapezoid"},
#     # Hard
#     {"topic": "Quadrilaterals", "level": "hard", "question": "In a rhombus with diagonals 6cm and 8cm, area is:", "options": ["12cm²", "24cm²", "36cm²", "48cm²"], "answer": "24cm²"}
# ]

# # --- Circle ---
# circle = [
#     # Easy
#     {"topic": "Circle", "level": "easy", "question": "What is the distance from center to edge of circle?", "options": ["Diameter", "Radius", "Chord", "Arc"], "answer": "Radius"},
#     {"topic": "Circle", "level": "easy", "question": "Circumference formula is:", "options": ["2πr", "πr²", "πd²", "2πd"], "answer": "2πr"},
#     {"topic": "Circle", "level": "easy", "question": "A line through circle touching two points is:", "options": ["Radius", "Chord", "Sector", "Segment"], "answer": "Chord"},
#     # Medium
#     {"topic": "Circle", "level": "medium", "question": "Area of circle with radius 3 units is:", "options": ["6π", "9π", "12π", "18π"], "answer": "9π"},
#     {"topic": "Circle", "level": "medium", "question": "Central angle of semicircle is:", "options": ["90°", "120°", "180°", "270°"], "answer": "180°"},
#     # Hard
#     {"topic": "Circle", "level": "hard", "question": "Area of sector with radius 5 and 60° central angle is:", "options": ["(25/6)π", "(5/2)π", "(25/3)π", "10π"], "answer": "(25/6)π"}
# ]

# # --- Area of Shapes ---
# area = [
#     # Easy
#     {"topic": "Area of Shapes", "level": "easy", "question": "Area of rectangle with length 5 and width 4?", "options": ["9", "18", "20", "25"], "answer": "20"},
#     {"topic": "Area of Shapes", "level": "easy", "question": "Area formula for triangle is:", "options": ["base×height", "½base×height", "πr²", "length×width"], "answer": "½base×height"},
#     {"topic": "Area of Shapes", "level": "easy", "question": "Area of square with side 3cm is:", "options": ["6cm²", "9cm²", "12cm²", "15cm²"], "answer": "9cm²"},
#     # Medium
#     {"topic": "Area of Shapes", "level": "medium", "question": "Area of trapezoid with bases 4/6 and height 5 is:", "options": ["20", "25", "30", "50"], "answer": "25"},
#     {"topic": "Area of Shapes", "level": "medium", "question": "Area of parallelogram with base 7 and height 3 is:", "options": ["10", "15", "21", "28"], "answer": "21"},
#     # Hard
#     {"topic": "Area of Shapes", "level": "hard", "question": "Find area of right triangle with legs 5 and 12 units:", "options": ["30", "60", "78", "120"], "answer": "30"}
# ]

# # Combine all geometry topics
# all_questions += angles + triangles + quadrilaterals + circle + area

# # Insert into MongoDB
# from pymongo import MongoClient

# client = MongoClient("mongodb+srv://alasylkhh:admin@cluster0.6fmla.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# questions = client['questions']
# questions_geometry = questions['geometry']
# questions_geometry.insert_many(all_questions)

# print("✅ Successfully inserted 30 questions across 5 Geometry topics into MongoDB!")