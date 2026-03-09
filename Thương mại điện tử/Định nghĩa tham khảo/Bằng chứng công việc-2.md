(Proof of work)
# Khái niệm
là thuật toán được áp dụng trong cơ chế động thuận của mạng lưới blockchain. Cơ chế đồng thuận của Proof of work từng được sử dụng để xác minh giao dịch và tạo ra các block mới.
Khi người dùng tiền mã hoá muốn chuyển token cho nhau trên blockchain được phát triển dựa trên mô hình PoW, hệ thống mạng lưới của blockchain này sẽ sử dụng một số cái phân quyền để đưa các giao dịch vào một block cụ thể. Tuy nhiên, quá trình xác nhận và sắp xếp block yêu cầu sự tham gia của con người
![[image 1.png|662x255]] Công việc này được gọi là "đào block", thường do các "thợ đào" thực hiện. Nguyên lý cốt lõi của quá trình trong cơ chế PoW là giải quyết một "phương trình toán học phức tạp", với mục tiêu tìm ra cách giải quyết nhanh và hiệu quả nhất
## Phương trình toán phức tạp
là một loại thuật toán đòi hỏi khả năng tính toán mạnh mẽ từ máy tính để giải quyết.
 Các bài toán đào block trong cơ chế Proof of Work:
 - Hash Function: Quá trình tìm kiếm ẩn số đầu vào dựa trên kết quả đầu ra của hàm
 - Interger Factorization: Bài toán này liên quan đến việc tìm một số biết nó là tích của hai số khác
 - Guilded Tour Puzzle Protocol: Nếu serverf cảm thấy mình đang bị tấn công DDoS, nó sẽ cần phải tính toán lại hash của một số node theo thứ tự nhất định. Lúc này, bài toán sẽ là để **tìm một chuỗi các giá trị hash**
Với sự mở rộng của mạng lưới, đòi hỏi sức mạnh tính toán ngày càng cao. Điều này đẩy nhanh sự cần đến năng lực hash để giải quyết bài toán và đào Block. Do đó, độ khó của thuật toán đào token tăng lên, trở thành một trong những vấn đề nhạy cảm nhất trên blockchain hiện nay
# Kết cấu
## Hash
Hash từ block hiện tại được lưu trữ và sử dụng trong block tiếp theo. Điều này tạo ra một cuốn sổ cái gồm các block mắc nối với nhat mà không bị thay đổi vì thông tin từ mỗi block được bao gồm trong hash của block mới nhất. Đây là nơi mà Proof of Work phát huy tác dụng.
![[image-1 1.png]]
### Khái niệm
Hash là một con số hexa được mã hoá gồm 64 chữ số. Với công nghệ hiện đại, 1 hash có thể được tạo ra trong vài mili giây với một lượng dữ liệu lớn. Công việc của các thợ đào là cố găng tính toán kết quả đó, điều này mất rất nhiều thời gian theo thuật ngữ của máy tính
Đào là quá trình xác minh các giao dịch thông qua việc giải quyết các hash và nhận phần thưởng
## Nonce
Hash bao gồm một chuỗi các con số gọi là nonce, viết tắt của *number used once*. Khi một thợ đào ==chương trình trên node làm việc để giải quyết hash== bắt đầu khai thác, nó tạo ra 1 hash từ thông tin công khai có sẵn bằng cách sử dụng một nonce bằng 0
### Giải quyết bằng hash
Nếu hash nhỏ hơn mục tiêu mạng hiện tại, thợ đào đã thành công trong việc giải quyết hash đó. Mục tiêu mạng là một kết quả toán học của một công thức được chuyển đổi thành một số hexa quy định độ khó trong việc khai thác
Nếu hash lớn hơn mục tiêu, chương trình khai thác sẽ thêm một giá trị bằng 1 vào nonce và tạo ra một hash mới. Toàn bộ mạng lưới các thợ đào cố gắng giải quyết hash theo cách này
Trên blockchain của Bitcoin, thợ đào thành công giải quyết hash sẽ nhận được phần thưởng cho công việc đã làm
# Các thành phần cơ chế PoW
## Thợ đào
Các blockchain sử dụng PoW dựa vào một mạng lưới phân tán các máy tính gọi là node. Những node này có trách nhiệm quan trọng là chấp nhận các lô giao dịch từ các node khác và đề xuất hoặc xác nhận các khối giao dịch mới cho toàn bộ mạng lưới
Trong ngữ cảnh này, các node thường được gọi là thợ đào, vì họ cống hiến năng lực tính toán và tài nguyên để kiếm tiền ảo cơ bản của mạng lưới
"Work" trong PoW đại diện cho năng lực tính toán mà các node đóng góp để xác nhận một khối giao dịch mới. Sức mạnh này được thể hiện trong hàm băm mật mã SHA-256, tạo nên sự khác biệt cho PoW so với các cơ chế đồng thuận khác
Một thuật toán quan trọng, được gọi là điều chỉnh độ khó, đảm bảo mạng lưới mất một khoảng thời gian cố định để xác nhận các khối giao dịch mới. Điều chỉnh này diễn ra khoảng mỗi 2016 khối (2 tuần) để duy trì thời gian khối ổn định là 10 phút. Đáng chú ý, việc cá nhân người đào gia nhập hoặc rời khỏi mạng lưới không ảnh hưởng trực tiếp đến mức độ khó trong các khoảng thời gian ngắn
## Phần thưởng
Người đào sẽ nhân phần thưởng khi họ tìm ra một hash dưới ngưỡng được đặt ra bởi mạng lưới. Khi phát hiện ra một hash khối hợp lệ, người đào sẽ phổ biến thông tin này cho những người đào khác để xác nhận và tích hợp nhanh chóng vào bản sao blockchain của họ. Quá trình xác nhận này nhằm ngăn chặn các hành động gian lận như double-spending
Hiện nay, người đào nhận được một phần thưởng cố định là 6.25 BTC/block, cùng với các phí giao dịch người dùng. Cấu trúc thưởng này là động lực cho các thợ đào tranh giành tham gia vào hệ thống PoW, khuyến khích tính trung thực, vì bất kỳ cố gắng can thiệp vào hệ thống đều sẽ dẫn đến lãng phí tài nguyên
 Lượng thưởng này giảm một nửa sau mỗi 210,000 khối (khoảng 4 năm). Sự giảm sút này gọi là chu kỳ [halving](https://coin68.com/nhung-dieu-can-biet-ve-bitcoin-halving/), tạo ra lo ngại về nguy cơ làm giảm sự động viên của người đào nếu giá của Bitcoin không đủ đào kịp. Tuy nhiên, khi người đào rời mạng lưới, mức độ khó cũng theo đó điều chỉnh, từ đó giảm chi phí đào Bitcoin.
```widgets
type: quote
quote: Độ chính xác và tốc độ của Blockchain phụ thuộc đáng kể vào cơ chế Proof of Work
```
# Ưu điểm và nhược điểm của Proof of Work
## Ưu điểm
- Bảo vệ chống tấn công DDoS
	- PoW đặt ra giới hạn cao đối với mạng lưới. Để tấn công mạng lưới, người tấn công cần phải sử dụng một lượng lớn năng lực máy tính và mất rất nhiều thời gian tính toán. Mặc dù có thể tấn công, nhưng chi phí tấn công sẽ rất lớn
- Khả năng đào block
	- Khả năng năng lực máy tính giải quyết bài toán đào block quan trọng hơn việc số tiền trong ví nhiều đến mức nào
## Nhược điểm