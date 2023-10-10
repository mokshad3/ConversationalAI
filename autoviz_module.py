from autoviz.AutoViz_Class import AutoViz_Class
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.available

print(sns.style.available)


class AutoVisualizer:
    def __init__(self):
        self.AV = AutoViz_Class()

    def generate_auto_viz(self, csv_file_path):
        AV = AutoViz_Class()
        auto_viz_html = AV.AutoViz(
            csv_file_path,
            depVar='',
            dfte=None,
            header=0,
            verbose=0,
            lowess=False,
            chart_format='bokeh-server',
            max_rows_analyzed=150000,
            max_cols_analyzed=30,
        )
        return auto_viz_html
