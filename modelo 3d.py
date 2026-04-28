pip install plotly
import plotly.graph_objects as go
# Criar uma visualização interativa do modelo
mesh_plot = go.Mesh3d(
    x=mesh.vertices[:, 0],
    y=mesh.vertices[:, 1],
    z=mesh.vertices[:, 2],
    i=mesh.faces[:, 0],
    j=mesh.faces[:, 1],
    k=mesh.faces[:, 2],
    color='lightblue',
    opacity=0.8
)

fig = go.Figure(data=[mesh_plot])
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='data'
    ),
    title="Visualização 3D do Modelo STL"
)

fig.write_html("/mnt/data/turbina_sensor_view.html")
"/mnt/data/turbina_sensor_view.html"
