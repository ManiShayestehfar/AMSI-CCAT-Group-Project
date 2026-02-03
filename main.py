import actual2a
import actual2b

dataset = actual2a.generate_datasets()
actual2a.plot_point_cloud(dataset)
actual2b.compute_PH(dataset['concentric'][0], title="Concentric Circles")
actual2b.compute_PH(dataset['disjoint'][0], title="Disjoint Circles")
actual2b.compute_PH(dataset['adjacent'][0], title="Adjacent Circles")

dataset = actual2a.generate_datasets(noise_std=0.2)
actual2a.plot_point_cloud(dataset)
actual2b.compute_PH(dataset['concentric'][0], title="Concentric Circles")
actual2b.compute_PH(dataset['disjoint'][0], title="Disjoint Circles")
actual2b.compute_PH(dataset['adjacent'][0], title="Adjacent Circles")