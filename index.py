import pandas as pd
import plotly.graph_objects as go

# Datos
columns = ['id_origen', 'id_destino', 'fecha', 'monto']
data = [
    ['003', '002', '2024-12-10', '4523.23'],
    ['005', '001', '2024-12-10', '576.23'],
    ['001', '004', '2024-12-10', '123.23'],
    ['002', '003', '2024-12-10', '5467.23'],
    ['004', '003', '2024-12-10', '867.23'],    
    ['003', '001', '2024-12-13', '345.23'],
    ['005', '003', '2024-12-13', '465.23'],
    ['005', '004', '2024-12-13', '867.23'],
    ['001', '003', '2024-12-16', '71.23'],
    ['002', '001', '2024-12-16', '543.23'],
    ['003', '001', '2024-12-16', '567.23'],
    ['005', '003', '2024-12-16', '786.23'],
    ['005', '004', '2024-12-16', '867.23'],
    ['001', '002', '2024-12-16', '234.23'],
    ['004', '003', '2024-12-16', '453.23'],
]

df = pd.DataFrame(data, columns=columns)
df['monto'] = df['monto'].astype(float)

def crear_sankey(id_origen=None):
    filtered_df = df if id_origen is None else df[df['id_origen'] == id_origen]

    all_nodes = list(set(filtered_df['id_origen']).union(set(filtered_df['id_destino'])))
    node_map = {node: i for i, node in enumerate(all_nodes)}

    source_indices = filtered_df['id_origen'].map(node_map)
    target_indices = filtered_df['id_destino'].map(node_map)
    values = filtered_df['monto']

    custom_labels = filtered_df.apply(lambda row: f"Fecha: {row['fecha']}<br>Monto: {row['monto']}", axis=1)

    sankey_figure = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=all_nodes
        ),
        link=dict(
            source=source_indices,
            target=target_indices,
            value=values,
            customdata=custom_labels,
            hovertemplate='De %{source.label} a %{target.label}<br>%{customdata}<extra></extra>'
        )
    ))

    sankey_figure.update_layout(
        title_text=f"Flujo de montos {'para id ' + id_origen if id_origen else ''}",
        font_size=10
    )

    sankey_figure.show()

crear_sankey()
