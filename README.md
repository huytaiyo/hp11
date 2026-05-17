Xin chào thầy/cô và các bạn. Hôm nay em xin trình bày về dự án website thương mại điện tử HP11 được xây dựng bằng Django Framework.

Bài thuyết trình của em sẽ gồm hai phần chính. Phần đầu tiên là demo thực hành trực tiếp trên sản phẩm để giới thiệu các chức năng của hệ thống. Phần thứ hai là giải thích về cấu trúc source code và cách hệ thống hoạt động phía backend.

Dự án HP11 được xây dựng với mục tiêu tạo ra một website bán hàng trực tuyến có các chức năng cơ bản của một hệ thống e-commerce như xem sản phẩm, quản lý giỏ hàng và đặt hàng. Ngoài ra, dự án còn giúp nhóm thực hành quy trình phát triển phần mềm thực tế, làm việc với GitHub và áp dụng Django vào xây dựng web backend.

Đầu tiên, em xin giới thiệu phần giao diện và chức năng của hệ thống.

Khi truy cập vào website, người dùng sẽ nhìn thấy trang chủ hiển thị danh sách sản phẩm. Tại đây, người dùng có thể xem hình ảnh, tên sản phẩm và giá bán. Giao diện được thiết kế đơn giản để người dùng dễ thao tác và tìm kiếm thông tin sản phẩm nhanh hơn.

Tiếp theo là chức năng xem chi tiết sản phẩm. Khi người dùng nhấn vào một sản phẩm, hệ thống sẽ hiển thị đầy đủ thông tin như hình ảnh lớn, mô tả chi tiết, giá bán và các thông tin liên quan. Chức năng này được xử lý bằng cách backend truy vấn dữ liệu từ database rồi trả kết quả ra giao diện cho người dùng.

Sau đó là chức năng giỏ hàng. Người dùng có thể thêm sản phẩm vào giỏ, cập nhật số lượng hoặc xóa sản phẩm khỏi giỏ hàng. Hệ thống sẽ tự động tính tổng tiền dựa trên các sản phẩm đã chọn. Đây là một trong những chức năng quan trọng nhất của website thương mại điện tử vì nó hỗ trợ quá trình mua hàng của người dùng.

Tiếp theo là chức năng đặt hàng. Khi người dùng nhập thông tin mua hàng và xác nhận đơn hàng, hệ thống sẽ lưu dữ liệu vào database bao gồm thông tin người mua, sản phẩm, địa chỉ và tổng tiền. Sau đó admin có thể theo dõi và quản lý đơn hàng trong hệ thống.

Ngoài giao diện người dùng, hệ thống còn có trang quản trị của Django. Trang admin cho phép quản trị viên thêm, sửa hoặc xóa sản phẩm, quản lý người dùng và theo dõi đơn hàng. Một ưu điểm lớn của Django là framework này đã tích hợp sẵn hệ thống admin mạnh mẽ nên giúp tiết kiệm rất nhiều thời gian phát triển.

Sau phần demo sản phẩm, em xin trình bày về cấu trúc source code của hệ thống.

Dự án được xây dựng bằng Django nên có cấu trúc khá rõ ràng và dễ quản lý. Một file quan trọng của dự án là file manage.py. Đây là file dùng để chạy server, migrate database và thực hiện các lệnh quản lý của Django. Ví dụ như chạy project bằng lệnh python manage.py runserver hoặc migrate database bằng python manage.py migrate.

Hệ thống sử dụng SQLite3 làm cơ sở dữ liệu. SQLite phù hợp với các dự án học tập vì nhẹ, dễ sử dụng và không cần cài đặt server database riêng. Database được dùng để lưu thông tin sản phẩm, người dùng, đơn hàng và dữ liệu giỏ hàng.

Ngoài ra, dự án còn có file requirements.txt dùng để quản lý các thư viện cần thiết. Trong đó có Django và Pillow. Khi clone project từ GitHub về máy, chỉ cần chạy lệnh pip install -r requirements.txt là có thể cài đặt toàn bộ thư viện để chạy hệ thống.

Django hoạt động theo mô hình MVT gồm Model, View và Template. Model dùng để làm việc với database. View dùng để xử lý logic nghiệp vụ. Template dùng để hiển thị giao diện cho người dùng. Quy trình hoạt động của hệ thống là người dùng gửi request lên server, View sẽ xử lý logic, Model truy vấn dữ liệu từ database rồi cuối cùng Template hiển thị kết quả ra giao diện.

Trong quá trình phát triển, nhóm sử dụng Git và GitHub để quản lý source code và làm việc nhóm. GitHub giúp lưu trữ code, theo dõi lịch sử thay đổi và hỗ trợ làm việc theo branch để tránh conflict khi nhiều người cùng chỉnh sửa hệ thống.

Tuy nhiên, trong quá trình thực hiện dự án, nhóm cũng gặp nhiều khó khăn như làm quen với Django Framework, xử lý migrate database và conflict khi merge source code. Nhưng nhờ quá trình tìm hiểu tài liệu và làm việc nhóm, nhóm đã dần giải quyết được các vấn đề đó.

Sau khi hoàn thành, hệ thống đã hoạt động ổn định với các chức năng cơ bản của một website thương mại điện tử. Qua dự án này, nhóm học được thêm nhiều kiến thức về phát triển web backend, quản lý cơ sở dữ liệu, làm việc nhóm và sử dụng GitHub trong thực tế.

Trong tương lai, hệ thống có thể được mở rộng thêm các chức năng như thanh toán online, dashboard thống kê, responsive mobile hoặc deploy lên cloud/server thực tế để phục vụ nhiều người dùng hơn.

Trên đây là phần trình bày của em về dự án HP11. Em xin cảm ơn thầy/cô và các bạn đã lắng nghe. Rất mong nhận được ý kiến đóng góp và câu hỏi từ mọi người.
