import streamlit as st
import time

st.set_page_config(page_title = '공부용 타이머', page_icon = '📖')

st. title('📖공부 타이머⏰')
st.divider()

#m = st.number_input('**시간을 입력해 주세요(분)**', min_value = 15, value = 30, max_value = 125, step = 5)
time_set = st.empty()
st.session_state['timer_time'] = time_set.number_input('**시간을 입력해 주세요(분)**', min_value = 15, value = 30, max_value = 125, step = 5)

timer_hours = st.session_state.timer_time//60
st.session_state['timer_hours'] = timer_hours
timer_mins = st.session_state.timer_time%60
st.session_state['timer_mins'] = timer_mins
timer_secs = 00
st.session_state['timer_secs'] = timer_secs

stop_hours = 0
st.session_state['stop_hours'] = stop_hours
stop_mins = 0
st.session_state['stop_mins'] = stop_mins
stop_secs = 0
st.session_state['stop_secs'] = stop_secs

#st.title(f'{hours:02}:{mins:02}.')
st.markdown(f"<h1 style='text-align: center;', style = 'font-size: 300px;'>{timer_hours:02}:{timer_mins:02}:{timer_secs:02}</h1>",
    unsafe_allow_html=True)
#st.button('**타이머 시작!**')
#st.write(f'**총 공부 시간: {stop_hours:02}:{stop_mins:02}:{stop_secs:02}**')
#st.write(f'**총 공부 시간: {st.session_state.stop_hours:02}:{st.session_state.stop_mins:02}:{st.session_state.stop_secs:02}**')
stopwatch = st.empty()
stopwatch.write(f'**총 공부 시간: {st.session_state.stop_hours:02}:{st.session_state.stop_mins:02}:{st.session_state.stop_secs:02}**')

if st.button('**타이머 시작!**'):
    time_set.empty()
    while True:
        time.sleep(1)
        st.session_state.stop_secs+=1
        st.session_state.timer_secs-=1
        if st.session_state.timer.secs==0:
            st.session_state.timer.secs == 59
            st.session_state.timer_mins -= 1
            


        stopwatch.write(f'**총 공부 시간: {st.session_state.stop_hours:02}:{st.session_state.stop_mins:02}:{st.session_state.stop_secs:02}**')
        if st.session_state.stop_secs ==60:
            st.session_state.stop_mins+=1
            st.session_state.stop_secs = 0
            stopwatch.write(f'**총 공부 시간: {st.session_state.stop_hours:02}:{st.session_state.stop_mins:02}:{st.session_state.stop_secs:02}**')
        if st.session_state.stop_mins == 60:
            st.session_state.stop_hours += 1
            st.session_state.stop_mins = 0
            stopwatch.write(f'**총 공부 시간: {st.session_state.stop_hours:02}:{st.session_state.stop_mins:02}:{st.session_state.stop_secs:02}**')

        


        


            
