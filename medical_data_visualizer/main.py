from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

# Generate and show the categorical plot
cat_plot = draw_cat_plot()
cat_plot.savefig("catplot.png")
plt.show()

# Generate and show the heatmap
heat_map = draw_heat_map()
heat_map.savefig("heatmap.png")
plt.show()
