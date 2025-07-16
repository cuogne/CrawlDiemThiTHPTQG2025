### Script crawl điểm thi thptqg 2025

- Crawl từ: https://diemthi.vnexpress.net/index/detail/sbd/{sbd}/year/2025 vì trang dò điểm của bộ dính captcha nên khó crawl dc (thay {sbd} bằng số báo danh thật)

- Vì lười nên chỉ crawl chơi 1 vài điểm thi, ai rảnh thì sửa url lại để crawl thêm nhé

### Thư viện

```terminal
pip3 install requests beautifulsoup4
```

### Chạy script

```terminal
python3 crawl.py
```

Dữ liệu dc crawl sẽ được lưu trong file `list_students.json`