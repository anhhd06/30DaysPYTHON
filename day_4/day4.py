#1.Nối chuỗi 'Thirty', 'Days', 'Of', 'Python' thành một chuỗi duy nhất, 'Thirty Days Of Python'.
a = 'Thirty'
b= 'Days'
c = 'Of'
d= 'Python'
print(a+' '+b +' '+c +' '+d)


#2.Nối chuỗi 'Coding', 'For', 'All' thành một chuỗi duy nhất, 'Coding For All'.

#Khai báo một biến có tên là company và gán cho nó giá trị ban đầu là "Coding For All".
#In biến company bằng hàm print() .
#In ra độ dài của chuỗi "company" bằng cách sử dụng phương thức `len()` và `print()` .
#Sử dụng phương thức `upper()` để chuyển tất cả các ký tự thành chữ in hoa .
#Hãy chuyển tất cả các ký tự thành chữ thường bằng phương thức lower() .
#Sử dụng các phương thức capitalize(), title(), swapcase() để định dạng giá trị của chuỗi " Coding For All" .
#Cắt bỏ từ đầu tiên của chuỗi "Coding For All" .
company = 'Coding For All'
index = company.find(' ')
company = company[index + 1:]
print(company)

#Chỉ số cuối cùng của chuỗi "Coding For All" là gì ?
#Ký tự nào nằm ở vị trí thứ 10 trong chuỗi "Coding For All"?
#Hãy tạo một từ viết tắt hoặc chữ viết tắt cho tên 'Coding For All'.
#Sử dụng chỉ mục để xác định vị trí xuất hiện đầu tiên của chữ C trong Coding For All.
#Sử dụng chỉ mục để xác định vị trí xuất hiện đầu tiên của chữ F trong Coding For All.
#Sử dụng lệnh rfind để xác định vị trí xuất hiện cuối cùng của chữ l trong cụm từ "Coding For All People".
company = 'Coding For All'
print( company.find('C'))
print( company.find('F'))
print("Coding For All People".rfind('l'))

print(f"{'Name':<15}{'Age':<8}{'Country':<10}{'City'}")

print(f"{'Asabeneh':<15}{'250':<8}{'Finland':<10}{'Helsinki'}")
#Danh sách sau đây chứa tên của một số thư viện Python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Nối các phần tử trong danh sách bằng một chuỗi chứa dấu cách.
List = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(List))


radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius %d is %.0f meters square." %(radius,area) )
print('The area of a circle with radius {} is {} meters square.'.format( radius,int(area) ) )
