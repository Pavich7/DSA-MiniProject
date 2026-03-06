import csv
from collections import defaultdict

class FacultyLoadSearchEngine:
    def __init__(self, csv_file):
        self.courses = {}
        self.lecturer_load = defaultdict(int)
        self.load_data(csv_file)

    def load_data(self, csv_file):
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                course_code = row["CourseCode"]
                name = row["Name"]
                credit = int(row["Credit"].split("(")[0])
                lecturers = [lec.strip() for lec in row["Lecturer"].split(",")]

                if course_code in self.courses:
                    self.courses[course_code]["Lecturers"].extend(lecturers)
                    self.courses[course_code]["Lecturers"] = list(set(self.courses[course_code]["Lecturers"]))
                else:
                    self.courses[course_code] = {
                        "Name": name,
                        "Credits": credit,
                        "Lecturers": lecturers
                    }

                for lec in lecturers:
                    self.lecturer_load[lec] += credit

    def find_course(self, course_code):
        if course_code in self.courses:
            course = self.courses[course_code]
            print(f"Name: {course['Name']}")
            print(f"Credits: {course['Credits']}")
            print("Lecturers:", ", ".join(course['Lecturers']))
        else:
            print("Course not found.")

    def report_load(self):
        for lecturer, total in self.lecturer_load.items():
            print(f"Lecturer: {lecturer} | Total Load: {total} Credits")

if __name__ == "__main__":
    engine = FacultyLoadSearchEngine("CprE_Subject.csv")
    print("Faculty Load & Search Engine")
    print("Type 'find_course <CourseCode>' or 'report_load'. Type 'exit' to quit.")
    while True:
        command = input(">> ").strip()
        if command == "exit":
            print("Bye bye!")
            break
        elif command.startswith("find_course"):
            parts = command.split()
            if len(parts) == 2:
                engine.find_course(parts[1])
            else:
                print("Usage: find_course <CourseCode>")
        elif command == "report_load":
            engine.report_load()
        else:
            print("Unknown command.")

# Btw, here are what we are using now:
# We are using hashmap cause it's efficient, O(1)!
# But we are using built-in dict in Python.