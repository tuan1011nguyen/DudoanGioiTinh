# Phân Loại Giới Tính từ Đặc Trưng Khuôn Mặt

## Giới thiệu
Dự án này tập trung vào việc phân loại giới tính dựa trên các đặc trưng khuôn mặt sử dụng các kỹ thuật học máy. Bộ dữ liệu bao gồm các đặc trưng như `long_hair` (tóc dài), `forehead_width_cm` (chiều rộng trán tính bằng centimet), `forehead_height_cm` (chiều cao trán tính bằng centimet), `nose_wide` (mũi rộng), `nose_long` (mũi dài), `lips_thin` (môi mỏng), và `distance_nose_to_lip_long` (khoảng cách từ mũi đến môi tính bằng centimet). Biến mục tiêu là `gender` (giới tính).

## Bộ dữ liệu
Bộ dữ liệu bao gồm các đặc trưng khuôn mặt và nhãn giới tính tương ứng. Dưới đây là mô tả ngắn gọn về các đặc trưng:

- `long_hair`: Đặc trưng nhị phân chỉ ra liệu người đó có tóc dài hay không.
- `forehead_width_cm`: Chiều rộng của trán tính bằng centimet.
- `forehead_height_cm`: Chiều cao của trán tính bằng centimet.
- `nose_wide`: Đặc trưng nhị phân chỉ ra liệu mũi có rộng hay không.
- `nose_long`: Đặc trưng nhị phân chỉ ra liệu mũi có dài hay không.
- `lips_thin`: Đặc trưng nhị phân chỉ ra liệu môi có mỏng hay không.
- `distance_nose_to_lip_long`: Khoảng cách từ mũi đến môi tính bằng centimet.

## Mô hình
Ba mô hình học máy khác nhau được sử dụng cho việc phân loại giới tính:

1. **Mạng Nơ-ron Nhân Tạo (ANN)**
   - Sử dụng kiến trúc mạng nơ-ron cho việc phân loại.
   - Được triển khai bằng các thư viện như TensorFlow hoặc PyTorch.
   - Điều chỉnh các tham số mô hình để tối ưu hóa độ chính xác phân loại.

2. **Cây Quyết Định**
   - Thuật toán cây quyết định cho việc phân loại.
   - Học một loạt các quy tắc quyết định if-else từ dữ liệu huấn luyện.
   - Dễ bị quá mức nếu không được cắt tỉa một cách phù hợp.

3. **Perceptron**
   - Một mạng nơ-ron một tầng sử dụng cho phân loại nhị phân.
   - Học các trọng số cho các đặc trưng để phân loại đầu vào vào hai lớp.
   - Đơn giản nhưng hiệu quả cho dữ liệu tách biệt tuyến tính.

4. **Kết Hợp Stacking**
   - Sự kết hợp của nhiều mô hình cơ sở với một mô hình meta (ví dụ: hồi quy logistic, mạng nơ-ron) để cải thiện hiệu suất.
   - Các mô hình cơ sở: ANN, Cây Quyết Định, Perceptron.
   - Mô hình meta học cách kết hợp dự đoán từ các mô hình cơ sở.

## Sử Dụng
1. Đảm bảo bạn đã cài đặt các phụ thuộc cần thiết (ví dụ: TensorFlow, scikit-learn).
2. Sao chép kho dự án và di chuyển đến thư mục dự án.
3. Chạy các tập lệnh để huấn luyện và đánh giá từng mô hình.
4. Thử nghiệm với các siêu tham số và kỹ thuật kỹ thuật đặc trưng để cải thiện hiệu suất.
5. Sử dụng kỹ thuật kết hợp stacking để kết hợp các dự đoán từ nhiều mô hình.

## Người Đóng Góp
- Nguyễn Đức Tuấn



## Cảm Ơn
Đề cập đến bất kỳ tài liệu tham khảo, bộ dữ liệu hoặc hướng dẫn nào bạn thấy hữu ích.
Cảm ơn bất kỳ cá nhân hoặc tổ chức nào đã đóng góp vào dự án.
