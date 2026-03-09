==(Chuỗi khối)==
Mỗi thông tin đều chứa thông tin về thời gian khởi tạo và được liên kết với khối trước đó, kèm theo mã thời gian và dữ liệu giao dịch
![[Blockchain.png]] Blockchain được tạo ra để chống lại sự thay đổi của dữ liệu
> Một khi dữ liệu đã được mạng lưới chấp nhận thì sẽ không có cách nào thay đổi được nó
# Tổng quan
## Thiết kế và mục đích
- Blockchain được đảm bảo nhờ cách thiết kế sử dụng hệ thống tính toán phân cấp với khả năng chịu lỗi [byzantine](https://vi.wikipedia.org/wiki/B%C3%A0i_to%C3%A1n_c%C3%A1c_v%E1%BB%8B_t%C6%B0%E1%BB%9Bng_Byzantine) (Byzantine Generals's Error).
- Blockchain phù hợp để ghi lại những sự kiện, hồ sơ y tế, xử lý giao dịch, công chứng, danh tính và chứng minh nguồn gốc
## Lịch sử
- Được phát minh bới [Satoshi Nakamoto](https://vi.wikipedia.org/wiki/Satoshi_Nakamoto) (2008) và trở thành một phần cốt lõi của Bitcoin
	- Đóng vai trò như cuốn sổ cái cho tất cả giao dịch
- Giải quyết được vấn đề double spending
## Đặc điểm
![[Bitcoin's Data Structure.png|450]] Công nghệ **Blockchain** tương đồng với cơ sở dữ liệu, chỉ khác với việc tương tác với cơ sở dữ liệu.
### đỊNH NGHĨA
- Chuỗi Khối (Blockchain)
- Cơ chế đồng thuận phân tán đồng đẳng (Distributed)
- Tính toán tin cậy (Trusted Computing)
- Hợp đồng thông minh (Smart contracts)
- Bằng chứng công việc (Proof of work)
#### Cơ chế đồng thuận phân tán đồng đẳng
Khi một cơ sở dữ liệu tập trung được dùng để quản lý việc xác thực giao dịch.
- Sử dụng mạng lưới các nút (nodes) để quyết định sự đồng thuận
- Các nút trong mạng lưới tự xác minh và đạt được kết quả thoả thuận
##### Cơ chế hình thành
-  Các nút giao dịch sẽ được lưu trữ trên một khối công cộng, tạo nên một chuỗi độc nhất
- Mỗi khối kế tiếp chứa một băm độc nhất (hash) của mã trước đó
- Mã hoá (thông qua hàm hash) được sử dụng để ==đảm bảo tính xác thực== của nguồn giao dịch và **loại bỏ** sự cần thiết phải có ==một trung gian tập trung==(dấu hiệu của cơ chế đồng thuận tập trung)
- Sự kết hợp mã hoá và công nghệ blockchain lại đảm bảo rằng sẽ không bao giờ có một giao dịch được lưu trữ 2 lần (lỗi double spending)
#### Chuỗi khối và dịch vụ chuỗi khối
Dịch vụ lưu trữ chuỗi khối có thể là một [số dư](https://vi.wikipedia.org/wiki/S%E1%BB%91_d%C6%B0) [tiền mã hoá](https://vi.wikipedia.org/wiki/Ti%E1%BB%81n_m%C3%A3_h%C3%B3a). Một chuỗi khối hoạt động như một hệ thống lưu chuyển giá trị thay thế mà không có một cá nhân hay tổ chức bên thứ ba thay đổi được.
Chuỗi khối được dựa trên quyền công khai và bí mật, nhìn công khai nhưng kiểm soát bí mật
#### Hợp đồng thông minh và tài sản thông minh
##### Hợp đồng thông minh
là các thoả thuận kỹ thuật số được lưu trữ và thực thi trên blockchain, tự động hoá các điều khoản hợp đồng mà không cần bên trung gian.
- Được dựa trên quy tắc "nếu/khi...thì..." (if...then...) được mã hoá bằng ngôn ngữ máy tính và được thực thi tự động khi các điều kiện xác minh trước được áp dụng
- Mục đích của hợp đồng là tăng cường hiệu quả, giảm chi phí và loại bỏ sự cần thiết của các bên trung gian
- Cách thức hoạt động
	- Khi các điều kiện được xác định trước trong mã nguồn được đáp ứng và được xác minh bởi mạng lưới blockchain, hợp đồng sẽ tự động thực hiện các hành động được chỉ định
	- Như hợp đồng truyền thống, hợp đồng thông minh có
		- Quy tắc
		- Điều kiện
		- Hậu quả
#### Tính toán tin cậy
```widgets
type: quote
quote: We own your personal devices and data and WE will determine what is right and wrong
author: 
```
là một công nghệ được phát triển và quảng bá bởi Trusted Computing Group.
### [[Bằng chứng công việc]] (Proof of work)
##### Cơ chế hoạt động
- Giải bài toán: Sử dụng sức mạnh máy tính để giải một bài toán mật mã
- Tiêu thụ năng lượng: Việc giải bài toán đòi hơi nhiều tài nguyên và năng lượng điện năng để tính toán
- Xác minh và nhận thưởng: Người giải được bài toán nhanh nhất sẽ xác nhận các giao dịch trong khối mới và nhận phẩn thưởng là tiền mã hoá
- Đảm bảo an ninh