# ==============================================================================
# The Developers Arena - Week 2 Project: Student Grade Calculator
# Name: Yogender Shamrao Hatkar
# Description: Processes multiple student marks, validates inputs, generates
#              grades with comments, provides class statistics, and file export.
# ==============================================================================

import os

def calculate_grade(average):
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', 'Very Good! You\'re doing well.'
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from teacher.'

def get_valid_number(prompt, min_val=0, max_val=100):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def save_results_to_file(student_names, student_results):
    try:
        with open("results_sample.txt", "w") as f:
            f.write("="*60 + "\n")
            f.write("                  STUDENT REPORT CARD                  \n")
            f.write("="*60 + "\n")
            f.write(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | {'Comment'}\n")
            f.write("-"*60 + "\n")
            for i in range(len(student_names)):
                name = student_names[i]
                avg = student_results[i]['average']
                grade = student_results[i]['grade']
                comment = student_results[i]['comment']
                f.write(f"{name:<20} | {avg:>5.1f} | {grade:^5} | {comment}\n")
        print("\n💾 Results have been successfully saved to 'results_sample.txt'!")
    except Exception as e:
        print(f"⚠️ Error saving file: {e}")

def search_student(student_names, student_results):
    print("\n--- 🔍 SEARCH STUDENT RECORD ---")
    query = input("Enter the student name to search: ").strip().lower()
    found = False
    for i in range(len(student_names)):
        if student_names[i].lower() == query:
            print(f"\n✨ Record Found:")
            print(f"👤 Name: {student_names[i]}")
            print(f"📊 Average Marks: {student_results[i]['average']:.1f}")
            print(f"🎓 Grade: {student_results[i]['grade']}")
            print(f"💬 Remarks: {student_results[i]['comment']}")
            found = True
            break
    if not found:
        print("❌ Student record not found in the database.")

def main():
    student_names = []
    student_marks = []
    student_results = []
    
    print("-" * 50)
    print("        STUDENT GRADE CALCULATOR INTERACTIVE        ")
    print("-" * 50)
    
    while True:
        try:
            num_students = int(input("Enter number of students to process: "))
            if num_students > 0:
                break
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    for i in range(num_students):
        print(f"\n--- STUDENT {i+1} ---")
        name = input("Student name: ").strip()
        while name == "":
            print("Name cannot be empty!")
            name = input("Student name: ").strip()
        
        student_names.append(name)
        
        print("Enter marks (0-100):")
        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")
        
        student_marks.append([math, science, english])
        
        average = (math + science + english) / 3
        grade, comment = calculate_grade(average)
        
        student_results.append({
            'average': average,
            'grade': grade,
            'comment': comment
        })

    while True:
        print("\n" + "="*50)
        print("                 MAIN DASHBOARD                 ")
        print("="*50)
        print("1. Display Results Table Summary")
        print("2. Display Comprehensive Class Statistics")
        print("3. Search a Specific Student")
        print("4. Save Results and Exit")
        print("="*50)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            print("\n" + "=" * 60)
            print("                        RESULTS SUMMARY                        ")
            print("=" * 60)
            print(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | {'Comment'}")
            print("-" * 60)
            for i in range(num_students):
                print(f"{student_names[i]:<20} | {student_results[i]['average']:>5.1f} |  {student_results[i]['grade']:^3}  | {student_results[i]['comment']}")
            print("=" * 60)
            
        elif choice == '2':
            if num_students > 0:
                averages = [res['average'] for res in student_results]
                class_avg = sum(averages) / len(averages)
                max_avg = max(averages)
                min_avg = min(averages)
                max_index = averages.index(max_avg)
                min_index = averages.index(min_avg)
                
                print("\n" + "=" * 50)
                print("                 CLASS STATISTICS                 ")
                print("=" * 50)
                print(f"Total Students processed : {num_students}")
                print(f"Overall Class Average     : {class_avg:.1f}")
                print(f"Highest Average Achieved  : {max_avg:.1f} ({student_names[max_index]})")
                print(f"Lowest Average Achieved   : {min_avg:.1f} ({student_names[min_index]})")
                print("=" * 50)
                
        elif choice == '3':
            search_student(student_names, student_results)
            
        elif choice == '4':
            save_results_to_file(student_names, student_results)
            print("\nThank you for using the Student Grade Calculator! Goodbye!")
            break
        else:
            print("Invalid Choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
  
