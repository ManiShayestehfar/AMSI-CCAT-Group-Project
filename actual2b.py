import gudhi
import matplotlib.pyplot as plt
import actual2a


def compute_PH(points, title="Point Cloud"):
    alpha_complex = gudhi.AlphaComplex(points=points)
    st_a = alpha_complex.create_simplex_tree()
    st_a.compute_persistence()
    PH_alpha = st_a.persistence()
    ax = gudhi.plot_persistence_barcode(PH_alpha, legend=True)
    ax.set_title("Alpha Complex Persistence Barcode for " + title)
    plt.show()
    #return PH_alpha




    

