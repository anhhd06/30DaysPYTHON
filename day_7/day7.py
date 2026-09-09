'''Tạo một tuple rỗng
Tạo một bộ dữ liệu chứa tên của các chị em gái và anh em trai của bạn (anh chị em tưởng tượng cũng được).
Ghép các cặp anh chị em ruột lại với nhau và gán chúng cho các anh chị em ruột.
Bạn có bao nhiêu anh chị em?
Chỉnh sửa bộ dữ liệu anh chị em ruột và thêm tên cha và mẹ của bạn vào đó, rồi gán nó cho biến family_members.'''


tup = ()
my_sister = ('Yen','Giang')
my_brother = ('Viet','An','Dung')
bro_and_sis = my_sister + my_brother
print(len(bro_and_sis))
family_members = list(bro_and_sis)
family_members.append('Hai')
family_members.append('Lam')
print(family_members)


'''Tách anh chị em ruột và cha mẹ khỏi family_members
Tạo các bộ dữ liệu gồm trái cây, rau củ và sản phẩm động vật. Kết hợp ba bộ dữ liệu này và gán cho một biến có tên là food_stuff_tp.
Thay đổi tuple about food_stuff_tp thành danh sách food_stuff_lt.
Cắt bỏ phần tử hoặc các phần tử ở giữa từ bộ dữ liệu food_stuff_tp hoặc danh sách food_stuff_lt.
Cắt bỏ ba mục đầu tiên và ba mục cuối cùng khỏi danh sách food_stuff_lt.
Xóa hoàn toàn tuple food_stuff_tp
Kiểm tra xem một mục có tồn tại trong bộ dữ liệu (tuple) hay không:
Kiểm tra xem 'Estonia' có phải là một quốc gia Bắc Âu hay không.

Kiểm tra xem 'Iceland' có phải là một quốc gia Bắc Âu hay không.'''


fruits = ('apple','orange','watermelon','banana')
vegetables = ('tomato','patato')
animal_products = ('meat','milk','egg')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
del food_stuff_lt[0:3]
del food_stuff_lt[-3:]
print(food_stuff_lt)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
# Hồ Đình Ánh đẹp trai
print('Ho Dinh Anh dep trai')
