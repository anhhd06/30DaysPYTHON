'''Tạo một từ điển trống có tên là dog
Thêm tên, màu sắc, giống chó, chiều dài chân, tuổi vào từ điển chó.
Tạo một từ điển học sinh và thêm các khóa là first_name, last_name, gender, age, marital status, skills, country, city và address cho từ điển.
Tìm độ dài của từ điển học sinh
Lấy giá trị của các kỹ năng và kiểm tra kiểu dữ liệu, nó phải là một danh sách.
Điều chỉnh giá trị kỹ năng bằng cách thêm một hoặc hai kỹ năng.
Lấy danh sách các khóa từ điển.
Lấy các giá trị của từ điển dưới dạng danh sách
Chuyển đổi từ điển thành danh sách các bộ dữ liệu bằng phương thức items().
Xóa một trong các mục trong từ điển
Xóa một trong các từ điển'''

dog = {}
dog['name'] = 'Tom'
dog['color'] = 'yellow'
dog['breed'] = 'Shiba'
dog['age'] = 1
student = {'first_name':'Ho Dinh','last_name':'Anh','gender':'male','age':20,'marital':'false','skills':['C++','Python','Java']}
print(len(student))
print(type(student['skills']))
student['skills'].append('Html')
student['skills'].append('Css')
print(student['skills'])
keys_student = student.keys()
print(keys_student)
print(student.items())
student.popitem()
print(dog)
del dog



