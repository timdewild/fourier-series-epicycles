from xml.dom import minidom
import svg.path 
import numpy as np
import matplotlib.pyplot as plt 

class SVGToCurve:
    
    def __init__(self, path_to_file: str, encoding = "UTF-8", sampling_density: int = 1000, scaled_x_range = 2):
        self.path_to_file = path_to_file
        self.encoding = encoding

        self.sampling_density = sampling_density
        self.scaled_x_range = scaled_x_range

        with open(self.path_to_file, encoding = "UTF-8") as xml_svg:
            doc =  minidom.parse(xml_svg)

            for path in doc.getElementsByTagName('path'):
                path_data = path.getAttribute('d')

        self.path = svg.path.parse_path(path_data)

        # generate rescaled path array
        self.t_array = np.linspace(0, 1, self.sampling_density)
        self.path_array = np.array([self.path.point(t) for t in self.t_array])

        self.xdata = self.path_array.real
        self.ydata = -self.path_array.imag

        # center x and y data
        self.xdata = self.xdata - np.mean(self.xdata)
        self.ydata = self.ydata - np.mean(self.ydata)

        # find x range for rescaling
        x_range = self.xdata.max() - self.xdata.min()

        # calculate scale factor
        scale_factor = self.scaled_x_range / x_range

        self.xdata = scale_factor * self.xdata
        self.ydata = scale_factor * self.ydata

    def get_xydata(self):
        return self.xdata, self.ydata

    def get_trace_function(self):

        def trace_function(t):
            return np.interp(t, self.t_array, self.xdata + 1j * self.ydata)
        
        return trace_function













