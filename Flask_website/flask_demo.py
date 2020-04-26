from flask import Flask, render_template

# instantiating the Flask Class
app = Flask(__name__)

# Decorator which ties to the function.
@app.route('/')
def home():
    # return "Homepage"
    return render_template("home.html")
# Another Decorator which ties to the function.
@app.route('/about/')
def home2():
    # return "About Flask Website"
    return render_template("about.html")

# Decorator which ties to the function.
@app.route('/plot/')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, output_file, show
    from bokeh.embed import components
    from bokeh.resources import CDN

    start_dt = datetime.datetime(2015, 11, 1)
    end_dt = datetime.datetime(2016, 3, 10)

    df = data.DataReader(name="GOOG", data_source="yahoo", start=start_dt, end=end_dt)

    def inc_dec(c, o):
        if (o > c):
            status = "Decrease"
        elif (o < c):
            status = "Increase"
        return status

    df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
    df["Middle"] = (df.Open + df.Close) / 2
    df["Height"] = abs(df.Open - df.Close)

    p = figure(x_axis_type="datetime", width=1000, height=300, sizing_mode="scale_width")
    p.title.text = "Candlestick Chart"
    p.grid.grid_line_alpha = 0.3

    p.segment(df.index, df.High, df.index, df.Low)

    hours_12_ms = 12 * 60 * 60 * 1000

    p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12_ms,
           df.Height[df.Status == "Increase"],
           fill_color="#7FFFD4", line_color="black")

    p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12_ms,
           df.Height[df.Status == "Increase"],
           fill_color="#FFB6C1", line_color="black")

    # js and html
    script1, div1 = components(p)

    # css--get that dynamacially in case version changes.
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files[0]
    return render_template("plot.html",script1=script1,div1=div1,cdn_js=cdn_js,cdn_css=cdn_css)

# If same current script is executed then __name is "main"
# If the current script is imported then __name is "script1"
if __name__=="__main__":
    app.run(debug = True)




