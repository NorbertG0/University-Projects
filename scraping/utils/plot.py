import plotly.express as px

def create_plot(data):
    plot_data = []
    for d in data:
        if d['type'] == 'City proper':
            plot_data.append({
                'Miasto': d['city'],
                'Rok': d['ref_year'],
                'Populacja': d['population']
            })

    fig = px.bar(
        plot_data,
        x='Miasto',
        y='Populacja',
        color='Rok',
        barmode='group',
        title='Polish City population',
        labels={'Populacja': 'Population', 'Miasto': 'City', 'Rok': 'Year'}
    )

    fig.update_layout(xaxis_tickangle=45)
    fig.show()