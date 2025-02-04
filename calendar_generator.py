from reportlab.lib.pagesizes import A4, landscape  # type: ignore
from reportlab.lib import colors  # type: ignore
from reportlab.pdfgen import canvas  # type: ignore
from datetime import datetime, timedelta


def get_date_from_week(reference_date, week_number, day_of_week):
    # Parse the reference date
    ref_date = datetime.strptime(reference_date, "%d.%m.%Y")

    # Calculate the start of the week for the reference date (Monday)
    start_of_week = ref_date - timedelta(days=ref_date.weekday())

    # Calculate the desired date by adding the number of weeks and days
    desired_date = (start_of_week +
                    timedelta(weeks=week_number - 1, days=day_of_week - 1))

    # Format the date as "dd.mm.yyyy"
    return desired_date.strftime("%d.%m.%Y")


# Function to compute booklet order
def get_booklet_order(total_pages):
    order = []
    left = 1
    right = total_pages
    while left < right:
        order.append(left)       # First side left page
        order.append(right)      # First side right page
        order.append(left + 1)   # Back side left page
        order.append(right - 1)  # Back side right page
        left += 2
        right -= 2
    return order


def draw_todo(c, x_week, y_week, h, w, r):
    # Define rectangle properties
    x = x_week  # X position
    y = y_week  # Y position (in ReportLab, (0,0) is bottom-left)
    corner_radius = 7  # Radius for rounded corners

    # Define circle properties
    circle_x = x_week + w + r + 1  # X center
    circle_y = y_week + r + 2  # Y center
    circle_radius = r

    y_ = y
    circle_y_ = circle_y
    for i in range(5):

        y_ = y - h*i
        circle_y_ = circle_y - i*(2*r + 4)

        # Draw a rounded rectangle
        c.roundRect(x, y_, w, h, corner_radius, stroke=1, fill=0)
        # Draw a circle
        c.circle(circle_x, circle_y_, circle_radius, stroke=1, fill=0)
    return y_ - h


def draw_meetings(c, x_week, y_week, h, w_time, w_desc):
    # Define rectangle properties
    x_start = x_week  # X position
    x_stop = x_week + w_time  # X position
    x_desc = x_week + 2*w_time  # X position
    y = y_week  # Y position (in ReportLab, (0,0) is bottom-left)
    corner_radius = 7  # Radius for rounded corners

    y_ = y
    for i in range(3):
        y_ = y - h*i
        # Draw start
        c.roundRect(x_start, y_, w_time, h, corner_radius, stroke=1, fill=0)
        # Draw stop
        c.roundRect(x_stop, y_, w_time, h, corner_radius, stroke=1, fill=0)
        # Draw desc
        c.roundRect(x_desc, y_, w_desc, h, corner_radius, stroke=1, fill=0)

    return y_


def draw_cross(c, area, spacing, cross_size):
    # Define grid area (adjust these values as needed)
    start_x, start_y = area["top_left"]  # Top-left corner of grid area
    end_x, end_y = area["bottom_right"]   # Bottom-right corner of grid area

    # Loop through the grid and draw crosses
    y = start_y
    while y > end_y:
        x = start_x
        while x < end_x:
            # Draw a cross centered at (x, y)
            c.line(x - cross_size / 2, y, x + cross_size / 2, y)  # H line
            c.line(x, y - cross_size / 2, x, y + cross_size / 2)  # V line
            x += spacing  # Move to the next column
        y -= spacing  # Move to the next row


def draw_day(c, area, date, ref_date):

    start_x, start_y = area["top_left"]  # Top-left corner of grid area
    end_x, end_y = area["bottom_right"]

    margin = 2
    box_h = 20
    radius = 8

    ###############
    #             #
    #  date line  #
    #             #
    ###############
    title_x = start_x + 57
    title_y = start_y - 20
    title_size = 12
    c.setFont("Helvetica-Bold", title_size)
    formatted_date = get_date_from_week(ref_date, date[0], date[1])
    c.drawString(title_x, title_y, formatted_date)
    ################
    #              #
    #  todos line  #
    #              #
    ################
    c.setLineWidth(1)
    todo_x = start_x+margin
    todo_y = start_y - 2*(box_h) - margin
    todo_h = box_h
    todo_w = (end_x - start_x) - 20
    y_meet = draw_todo(c, todo_x, todo_y, todo_h, todo_w, radius)
    ################
    #              #
    #   meet line  #
    #              #
    ################
    c.setLineWidth(1)
    meet_x = start_x + margin
    y_meet = y_meet - margin
    w_meet_date = 30
    w_meet_desc = (end_x - start_x) - 2*w_meet_date - margin
    y_cross = draw_meetings(c, meet_x, y_meet, box_h, w_meet_date, w_meet_desc)
    ################
    #              #
    #  cross line  #
    #              #
    ################
    spacing = 20
    cross_size = 3
    c.setLineWidth(0.7)
    area_cross = {"top_left": (start_x + margin, y_cross - cross_size),
                  "bottom_right": (start_x + (end_x - start_x)-margin, end_y)}
    draw_cross(c, area_cross, spacing, cross_size)


def draw_page(c, ref_date):
    # Set page size to landscape A4
    width, height = landscape(A4)
    front = True
    week_end = 52
    week_start = 1
    for page_nb in range(26):
        ##############
        #            #
        #  mid line  #
        #            #
        ##############
        # Draw a horizontal line in the middle
        c.setLineWidth(2)
        c.setStrokeColor(colors.black)
        c.line(0, height / 2, width, height / 2)
        ################
        #              #
        #  weeks line  #
        #              #
        ################
        # Draw 4 vertical lines with equal spacing
        vertical_spacing = width / 5  # Divide the page into 5 equal parts
        for j in range(1, 5):
            c.setLineWidth(2)
            x = j * vertical_spacing
            c.line(x, 0, x, height)

        if front:
            # top
            for i in range(5):
                area = {"top_left": (i*width/5, height),
                        "bottom_right": (i*width/5 + width/5, height/2)}
                date = (week_end, i+1)
                draw_day(c, area, date, ref_date)
            # bottom
            for i in range(5):
                area = {"top_left": (i*width/5, height/2),
                        "bottom_right": (i*width/5 + width/5, 0)}
                date = (week_start, i+1)
                draw_day(c, area, date, ref_date)
            front = False
        else:
            # top
            for i in range(5):
                area = {"top_left": (i*width/5, height),
                        "bottom_right": (i*width/5 + width/5, height/2)}
                date = (week_start, i+1)
                draw_day(c, area, date, ref_date)
            # bottom
            for i in range(5):
                area = {"top_left": (i*width/5, height/2),
                        "bottom_right": (i*width/5 + width/5, 0)}
                date = (week_end, i+1)
                draw_day(c, area, date, ref_date)
            front = True

        week_start += 1
        week_end -= 1

        c.showPage()


def generate_pdf(filename):
    c = canvas.Canvas(filename, pagesize=landscape(A4))
    ref_date = "10.02.2025"
    draw_page(c, ref_date)
    c.save()


if __name__ == "__main__":
    generate_pdf("foldable_daybook.pdf")
