import csv
from collections import defaultdict

class FacultyLoadSearchEngine: # Class T(n) = O(n) + O(n^2) + O(1) + O(n) = O(n^2)
    def __init__(self, csv_file): # T(n) = 2O(1) + O(n^2) = O(n^2)
        self.courses = {} # O(1)
        self.lecturer_load = defaultdict(int) # O(1)
        self.load_data(csv_file) # O(n^2)

    def load_data(self, csv_file): # T(n) = O(1) + O(n^2) = O(n^2)
        with open(csv_file, newline='', encoding='utf-8') as f: # O(1)
            reader = csv.DictReader(f) # O(1)
            # Read each row into courses dict and count lecturer load.
            for row in reader: # O(n^2)
                course_code = row["CourseCode"]
                name = row["Name"]
                credit = int(row["Credit"].split("(")[0])
                lecturers = [lec.strip() for lec in row["Lecturer"].split(",")]

                if course_code in self.courses: # O(1)
                    self.courses[course_code]["Lecturers"].extend(lecturers)
                    self.courses[course_code]["Lecturers"] = list(set(self.courses[course_code]["Lecturers"]))
                else:
                    self.courses[course_code] = {
                        "Name": name,
                        "Credits": credit,
                        "Lecturers": lecturers
                    }

                # Count load for each lecturer here...
                for lec in lecturers: # O(n)
                    self.lecturer_load[lec] += credit

    def find_course(self, course_code): # T(n) = O(1)
        if course_code in self.courses: # O(1)
            course = self.courses[course_code]
            print(f"Name: {course['Name']}")
            print(f"Credits: {course['Credits']}")
            print("Lecturers:", ", ".join(course['Lecturers']))
        else:
            print("Course not found.")

    def report_load(self): # T(n) = O(n)
        for lecturer, total in self.lecturer_load.items(): # O(n)
            print(f"Lecturer: {lecturer} | Total Load: {total} Credits")

if __name__ == "__main__":
    engine = FacultyLoadSearchEngine("CprE_Subject.csv") 
    print("Faculty Load & Search Engine")
    print("Type 'find_course <CourseCode>' or 'report_load'. Type 'exit' to quit.")
    # Loop to handle commands.
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

# What we are using now:
# We are using built-in dict in Python.
# Inside it, they are using hashmap, so the time complexity is O(1)!
