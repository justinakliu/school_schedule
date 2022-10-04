from school_schedule.student import Student

def test_student_class_attributes_are_accurate():
    student = Student("Ada", "Junior", ["Programming 101", "Big O Notation", "Art"])

    assert student.name == "Ada"
    assert student.grade == "Junior"
    assert student.classes == ["Programming 101", "Big O Notation", "Art"]

def test_student_class_with_empty_classes_attribute():
    student = Student("Ada", "Junior", [])

    assert student.classes == []
    assert len(student.classes) == 0

def test_add_class_adds_class_to_classes():
    student = Student("Ada", "Junior", ["Programming 101", "Big O Notation", "Art"])
    original_length = len(student.classes)
    
    student.add_class("Tae Kwon Do")

    assert len(student.classes) == original_length + 1
    assert student.classes[-1] == "Tae Kwon Do"
    assert student.classes == ["Programming 101", "Big O Notation", "Art", "Tae Kwon Do"]

def test_get_num_classes_returns_length():
    student = Student("Ada", "Junior", ["Programming 101", "Big O Notation", "Art"])
    length = len(student.classes)

    assert length == student.get_num_classes()

def test_empty_get_num_classes_returns_zero():
    student = Student("Ada", "Junior", [])

    assert student.get_num_classes() == 0

def test_display_classes_returns_classes_string():
    student = Student("Ada", "Junior", ["Programming 101", "Big O Notation", "Art"])
    
