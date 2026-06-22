import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def missing_value_chart(df: pd.DataFrame):
    missing = df.isna().sum().reset_index()
    missing.columns = ["column", "missing_count"]
    missing = missing[missing["missing_count"] > 0]
    if missing.empty:
        return None
    fig = px.bar(
        missing,
        x="column",
        y="missing_count",
        text="missing_count",
        title="Missing value analysis",
        template="plotly_dark",
    )
    fig.update_traces(marker_color="#f59e0b", hovertemplate="%{x}: %{y}<extra></extra>")
    fig.update_layout(height=340, margin=dict(l=0, r=0, t=30, b=0))
    return fig


def distribution_chart(df: pd.DataFrame, column: str, title: str):
    values = df[column].fillna("Missing").astype(str)
    counts = values.value_counts().reset_index()
    counts.columns = [column, "count"]
    if counts.empty:
        return None
    fig = px.bar(
        counts,
        x=column,
        y="count",
        text="count",
        title=title,
        template="plotly_dark",
    )
    fig.update_traces(marker_color="#38bdf8", hovertemplate="%{x}: %{y}<extra></extra>")
    fig.update_layout(height=360, margin=dict(l=0, r=0, t=30, b=0))
    return fig


def correlation_heatmap(df: pd.DataFrame):
    numeric = df.select_dtypes(include=["number"])
    if numeric.shape[1] < 2:
        return None
    corr = numeric.corr()
    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="Blues",
        title="Correlation heatmap",
        template="plotly_dark",
    )
    fig.update_layout(height=420, margin=dict(l=0, r=0, t=30, b=0))
    return fig


def confusion_matrix_chart(matrix, labels):
    fig = go.Figure(
        data=go.Heatmap(
            z=matrix,
            x=labels,
            y=labels,
            colorscale="Blues",
            hovertemplate="%{y} / %{x}: %{z}<extra></extra>",
        )
    )
    fig.update_layout(
        title="Confusion Matrix",
        xaxis_title="Predicted",
        yaxis_title="Actual",
        template="plotly_dark",
        height=420,
        margin=dict(l=0, r=0, t=30, b=0),
    )
    return fig
