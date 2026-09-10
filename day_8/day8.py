# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

'''Tìm độ dài của tập hợp it_companies
Thêm 'Twitter' vào it_companies
Thêm nhiều công ty CNTT cùng lúc vào tập hợp it_companies
Xóa một trong các công ty khỏi tập hợp it_companies
Sự khác biệt giữa "remove" và "discard" là gì?'''

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Fpt','Instargram'])
print(it_companies)
it_companies.pop()
print(it_companies)

'''Kết hợp A và B
Tìm giao điểm A và B
A có phải là tập con của B không?
A và B có phải là các tập hợp rời nhau không?
Nối A với B và B với A.
Hiệu đối xứng giữa A và B là gì?
Xóa hoàn toàn các bộ'''

C = A.union(B)
print(C)
D = A.intersection(B)
print(D)
print(A.issubset(B))
print(len(D)==0)
print(A.symmetric_difference(B))
del A
del B


'''Chuyển đổi các độ tuổi thành một tập hợp và so sánh độ dài của danh sách và tập hợp, tập hợp nào lớn hơn?
Giải thích sự khác biệt giữa các kiểu dữ liệu sau: chuỗi (string), danh sách (list), bộ dữ liệu (tuple) và tập hợp (set).
Tôi là một giáo viên và tôi thích truyền cảm hứng và dạy dỗ mọi người. Câu này có bao nhiêu từ độc đáo? Hãy sử dụng phương pháp tách từ và thiết lập để tìm ra các từ độc đáo.'''

age_list = list(age)
print('Danh sach dai hon: ',len(age_list) > len(age))
text ='I am a teacher and I love to inspire and teach people'
Docdao = set(text.split())
print(Docdao,len(Docdao))
