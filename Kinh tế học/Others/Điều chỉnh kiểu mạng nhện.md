# Khái niệm
Mô tả cách <font color="#ff0000">giá</font> và <font color="#ff0000">sản lượng</font> của một hàng hoá dao động theo thời gian, khi có độ trễ giữa thời điểm <font color="#ff0000">người sản xuất quyết định sản lượng</font> và <font color="#ff0000">thời điểm sản phẩm được đưa ra thị trường</font>
```widgets
type: quote
quote: Quyết định năm nay, hưởng chịu năm sau
```
- Bản chất: Mô tả sự dao động giá và sản lượng qua các chu kỳ thời gian
- Chủ thể quyết định: Nhà sản xuất
- Giả định quan trọng nhất
Người sản xuất tin rằng (một cách ngây thơ) giá của năm sau ($P_{t+1}$) sẽ bằng giá của năm nay ($P_{t}$) để quyết định sản lượng
$$
Q_{S,t+1} = f(P_{t})
$$
- Thời gian có độ trễ, cung của ngày hôm nay ($Q_{S}$) được quyết định bởi giá hôm qua ($P_{t-1}$)
# Cơ chế hoạt động
Giả sử thị trường bắt đầu từ một điểm không công bằng
**Chu kì 1: Khởi đầu từ Giá cao ($P_{1}$)**
1. Năm 1 (Giá cao): Giá thị trường năm nay là $P_{1}$ (cao hơn giá cân bằng $P^{*}$)
2. Quyết định năm 2 (Sản xuất): Người sản xuất tin rằng năm sau giá vẫn sẽ như $P_{1}$. Họ quyết định **Tăng sản lượng** lên $Q_{2}$ (tức là mọi người đổ xô sản xuất mặt hàng $P_{1}$)
3. Năm 2 (Thị trường): Sản lượng lớn $Q_{2}$ được đưa ra thị trường. Do $Q_{2}$ quá lớn (hàng tồn kho), thị trường bắt buộc phải **giảm giá** xuống $P_{2}$ nhằm giải quyết hàng tồn kho ($P_{2} \lt P^{*}$)
**Chu kì 2: Tiếp tục giá từ giá thấp ($P_{2}$)**
4. Năm 2 (Giá thấp): Giá thị trường hiện tại là $P_{2}$ (thấp hơn $P^{*}$, có thể lỗ)
5. Quyết định năm 3 (sản xuất): $P_{2}$ lỗ, người sản xuất tin rằng năm sau vẫn sẽ thấp => quyết định **giảm sản lượng** xuống $Q_{3}$ (tức là mọi người ngừng tiếp tục sản xuất)
6. Năm 3 (Thị trường): Sản lượng nhỏ $Q_{3}$ được đưa ra thị trường. Do $Q_{3}$ quá ít (thiếu hụt), thị trường buộc **tăng giá** lên $P_{3}$ ($P_{3} \gt P^{*}$)
Suy ra, cơ chế hoạt động của mạng nhện được hiểu theo cách:
Giá cao -> Sản lượng lớn -> Giá thấp -> Sản lượng nhỏ -> Giá cao
# Phân loại mạng nhện
- Độ co giãn ($E$)
- Cung ($S$)
- Cầu ($D$)

| Kiểu điều chỉnh | Quan hệ độ dốc, co giãn | Kết quả |
| --------------- | ----------------------- | ------- |
| Hội tụ          | Độ dốc $D$ dốc hơn $S$  |         |
| Phân kì         | Độ dốc $S$ dốc hơn $D$  |         |
| Chu kì vĩnh cửu | Độ dốc $S$ bằng $D$     |         |
