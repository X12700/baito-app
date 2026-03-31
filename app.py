import streamlit as st

def time_to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def create_time_list(start_h, end_h):
    times = []
    for h in range(start_h, end_h + 1):
        for m in [0, 15, 30, 45]:
            times.append(f"{h}:{m:02}")
    return times

start_list = create_time_list(9, 15)
end_list = create_time_list(11, 20)
rest_list = ["0:15","0:30","0:45","1:00","1:15","1:30","1:45","2:00","2:15","2:30"]

st.title("日当計算アプリ")

start = st.selectbox("開始時刻", start_list)
end = st.selectbox("終了時刻", end_list)
rest = st.selectbox("休憩時間", rest_list)
drive = st.selectbox("送迎時間", rest_list)

if st.button("計算"):
    start_m = time_to_minutes(start)
    end_m = time_to_minutes(end)
    rest_m = time_to_minutes(rest)
    drive_m = time_to_minutes(drive)

    work_m = end_m - start_m - rest_m

    if work_m < 0:
        st.error("入力ミスがあります")
    else:
        work_H = f"{work_m / 60:.2f}"
        normal_H = f"{(work_m - drive_m) / 60:.2f}"

        st.success(f"拘束時間: {work_H}時間")
        st.success(f"普通作業時間: {normal_H}時間")
