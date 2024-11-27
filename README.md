- chuẩn bị dữ liệu
   ### pwd  # crawl
   - cào video về bằng jupyter notebook trong crawl/
   - dùng ffmpeg chuyển video mp4 ở thư mục hiện tại sang audio wav lưu trong ngoclan/, loại bỏ hết khoảng trắng trong tên video
   ### ii=1;for i in *.mp4; do echo $i -------------- $ii.wav>>ffm.txt; ffmpeg -i $i ngoclan/$ii.wav -y;ii=$((ii+1));done  # mp4 to wav
   - tách giai điệu và ca từ bằng demucs
   ### cd ngoclan
   ### for i in *.wav; do demucs --two-stems=vocals $i; done
<h2>training</h2>
   - chia thành các audio con dựa trên khoảng lặng và cắt nhỏ audio con đó thành từng 10 giây trong sl.py
   ### cd audio-slicer 
   ### deactivate&&source venv/bin/activate
   ### python3 sl.py