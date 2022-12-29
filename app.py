
import tkinter as tkt
from helpers.destroy import destroy
from covid.home import total_no_of_cases_each_day, total_no_of_cases_each_month, areas_with_highest_cases, comparing_two_areas
from stop_and_search.home import stop_and_search_by_months, compare_stop_and_search_results_for_two_areas, ethnicity, by_gender

root = tkt.Tk()
root.geometry("600x600")
root.title("C2007438-Element 2")

frame_1 = tkt.Frame(root, width=400, height=360)
frame_1.place(x=140, y=150)
    
window_frame = tkt.Frame(root, width=490, height=80)
window_frame.place(x=30, y=70)

def render_covid_btns():
    destroy(window_frame)
    destroy(frame_1)
    tkt.Button(window_frame, text="Total number of cases each day" , command= lambda: total_no_of_cases_each_day(frame_1)).place(x=10, y=20)
    tkt.Button(window_frame, text="Total number of cases each month" , command=lambda: total_no_of_cases_each_month(frame_1)).place(x=240, y=20)
    tkt.Button(window_frame, text="Areas with highest cases each day" , command=lambda: areas_with_highest_cases(frame_1)).place(x=10, y=50)
    tkt.Button(window_frame, text="Comparing two areas" , command=lambda: comparing_two_areas(frame_1)).place(x=260, y=50)
    
def render_stop_and_search_btns(): 
    destroy(window_frame)
    destroy(frame_1)
    tkt.Button(window_frame, text="Stop and search by months" , command=lambda: stop_and_search_by_months(frame_1)).place(x=25, y=20)
    tkt.Button(window_frame, text="Summer stop and search result" , command=lambda: compare_stop_and_search_results_for_two_areas(frame_1)).place(x=230, y=20)
    tkt.Button(window_frame, text="By ethnicity" , command=lambda: ethnicity(frame_1)).place(x=110, y=50)
    tkt.Button(window_frame, text="By Gender" , command=lambda: by_gender(frame_1)).place(x=220, y=50)
    # tkt.Button(window_frame, text="By Gender" , command=compare_stop_and_search_results_for_two_areas).place(x=25, y=50)
    
    

tkt.Button(root, text="Covid dataset" , command=lambda: render_covid_btns()).place(x=160, y=40)
tkt.Button(root, text="Stop and Search", command= lambda: render_stop_and_search_btns()).place(x=290, y=40)

tkt.mainloop()
