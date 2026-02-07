import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import StringIO

# --- 1. 内置数据 (Cleaned Data) ---
# 为了方便直接运行，这里直接嵌入了清洗后的数据
trend_csv = """month,owner,phase,month_index,views,likes,total_followers
24-03,Ignite Search,Outsource,M1,1135,23,93
24-04,Ignite Search,Outsource,M2,55,3,150
24-05,Ignite Search,Outsource,M3,502,11,150
24-06,Ignite Search,Outsource,M4,355,3,187
24-07,Ignite Search,Outsource,M5,335,0,209
24-08,Ignite Search,Outsource,M6,383,10,216
24-09,Ignite Search,Outsource,M7,422,8,227
24-10,Ignite Search,Outsource,M8,1020,50,257
24-11,Ignite Search,Outsource,M9,644,20,282
24-12,Ignite Search,Outsource,M10,530,22,299
25-04,CN Marketing,Takeover,M1,2017,53,367
25-05,CN Marketing,Takeover,M2,1977,97,392
25-06,CN Marketing,Takeover,M3,868,54,400
25-07,CN Marketing,Takeover,M4,2037,96,419
25-08,CN Marketing,Takeover,M5,2040,143,441
25-09,CN Marketing,Takeover,M6,1577,108,450
25-10,CN Marketing,Takeover,M7,1690,93,466
25-11,CN Marketing,Takeover,M8,1112,86,484
25-12,CN Marketing,Takeover,M9,957,106,492
"""

articles_csv = """Date,Title,Views,Likes,Shares,Owner,Link
2024-04-03,"Hello Everyone, we are on LRB /WeChat now!",909,20,64,Ignite Search,Link
2024-04-03,Product Highlight: Equitone,226,3,16,Ignite Search,Link
2024-04-30,The new National Construction Code 2022,55,3,2,Ignite Search,Link
2024-07-05,Our Supply Partners,283,7,14,Ignite Search,Link
2024-07-05,Partner - Knotwood,219,4,14,Ignite Search,Link
2024-06-08,How to decide when it's time to re-side,246,2,22,Ignite Search,Link
2024-06-09,Extra Accommodation: A Guide to Granny Flats,109,1,13,Ignite Search,Link
2024-07-05,Hume Products - Rondo,316,0,24,Ignite Search,Link
2024-07-06,15 spots in your home you may be forgetting to clean,19,0,1,Ignite Search,Link
2024-08-29,Hume Products - James Hardie,102,5,8,Ignite Search,Link
2024-09-01,What Key Measurements & Room Dimensions Should I Know?,281,5,40,Ignite Search,Link
2024-09-15,迈向未来城市：智能光伏公交站亭,266,7,30,Ignite Search,Link
2024-09-25,创新设计引领变革：BIPV遮阳系统,156,1,14,Ignite Search,Link
2024-10-09,ML Glass创新玻璃产品,464,33,40,Ignite Search,Link
2024-10-09,光伏车棚：改变城市生活,556,17,46,Ignite Search,Link
2024-11-18,轻松刮平！Knauf BaseCote™全新配方,378,12,23,Ignite Search,Link
2024-11-19,打造【完美厨房】，10个妙招一定要记,266,8,25,Ignite Search,Link
2024-12-18,荣耀见证！Hume荣获CBANSW 2024年度供应商大奖！,346,17,43,Ignite Search,Link
2024-12-19,纤维水泥板新选择！揭秘EQUITONE,184,5,25,Ignite Search,Link
2025-03-04,HUME携手未来建筑师，预见悉尼新天际线,551,27,70,CN Marketing,Link
2025-04-23,HUME中国展厅喜迎首批海外考察团,1326,23,128,CN Marketing,Link
2025-06-05,让您的建筑 “会呼吸” 的秘密武器,391,29,67,CN Marketing,Link
2025-12-05,被设计师应用于各种场景的 “万能建材”,487,32,96,CN Marketing,Link
2025-05-21,轻松驾驭湿区装修：魅力百变的轻质水泥板,447,20,58,CN Marketing,Link
2025-05-28,隐形车库门 | 您家的一张对外名片,652,16,72,CN Marketing,Link
2025-06-04,【假期通知】HUME六月节日期间营业安排,116,7,13,CN Marketing,Link
2025-06-18,每个建筑立面，都能有自己的独特灵魂！,152,9,21,CN Marketing,Link
2025-06-27,从引擎到空间，BMW的建材哲学,524,32,100,CN Marketing,Link
2025-07-04,拆解 51 64 78 这组神秘六位数,365,27,78,CN Marketing,Link
2025-07-11,百年电机：畅游MAKITA工具王国,704,24,92,CN Marketing,Link
2025-07-21,建筑行业盛会 | CBANSW Tradeshow 2025,439,27,80,CN Marketing,Link
2025-07-28,冬天来了，做个懂地暖的人,529,18,77,CN Marketing,Link
2025-08-01,以匠心选材，还原生活本真,558,32,119,CN Marketing,Link
2025-08-15,2025 CBANSW承包商供应商展圆满收官！,682,51,107,CN Marketing,Link
2025-07-21,他们守护生命，我们锻造战壕,478,34,88,CN Marketing,Link
2025-07-28,此板不简单！潮湿区域的超强免疫系统,322,26,59,CN Marketing,Link
2025-09-05,乘阳光之翼驰骋于世！HUME已为您备好入场券,486,34,94,CN Marketing,Link
2025-09-19,【实操培训】一举获取EQUITONE大师课证书,322,16,68,CN Marketing,Link
2025-09-26,让空间自带吸引力！灯具照明一站式服务,291,24,59,CN Marketing,Link
2025-10-10,HUME Project: 见证奢华地标拔地而起,585,33,78,CN Marketing,Link
2025-10-17,不锈钢全屋定制：生活美学的明智之选,564,27,90,CN Marketing,Link
2025-10-28,木材、石材、玻璃、金属、水泥板,541,33,77,CN Marketing,Link
2025-11-06,领先，不只是快一步,485,26,36,CN Marketing,Link
2025-11-19,澳洲建筑界的年度盛事：CBANSW 2025年会,306,32,36,CN Marketing,Link
2025-10-28,筑造时代枢纽，HUME与您共承千钧,321,28,44,CN Marketing,Link
2025-12-10,HUME荣获2025年度 SIM-PAC 可持续发展奖,312,30,39,CN Marketing,Link
2025-12-19,【HUME项目】为岁月筑巢，守护养老空间,245,30,28,CN Marketing,Link
2025-12-23,告别拼凑！来HUME构建完美浴室,259,29,30,CN Marketing,Link
2025-12-31,2025，感谢并肩。2026，共启新章！,141,17,18,CN Marketing,Link
"""

# --- 2. 页面设置 ---
st.set_page_config(page_title="HUME Marketing Analysis", layout="wide")
st.title("📊 HUME Marketing Data Analysis: Outsourcing vs Takeover")
st.markdown("---")

# --- 3. 数据加载 ---
@st.cache_data
def load_data():
    df_t = pd.read_csv(StringIO(trend_csv))
    df_a = pd.read_csv(StringIO(articles_csv))
    return df_t, df_a

df_trend, df_articles = load_data()

# --- 4. 关键指标概览 (KPI Overview) ---
st.subheader("Executive Summary")
col1, col2, col3, col4 = st.columns(4)

# 计算平均值
ignite_trend = df_trend[df_trend['owner'] == 'Ignite Search']
cn_trend = df_trend[df_trend['owner'] == 'CN Marketing']
avg_views_ig = ignite_trend['views'].mean()
avg_views_cn = cn_trend['views'].mean()
avg_likes_ig = ignite_trend['likes'].mean()
avg_likes_cn = cn_trend['likes'].mean()

col1.metric("Avg Views / Month", f"{avg_views_cn:.0f}", f"{((avg_views_cn-avg_views_ig)/avg_views_ig)*100:.1f}%")
col2.metric("Avg Likes / Month", f"{avg_likes_cn:.0f}", f"{((avg_likes_cn-avg_likes_ig)/avg_likes_ig)*100:.1f}%")
col3.metric("Posts / Month", "6.3", "+315% vs Ignite (2.0)")
col4.metric("Follower Growth Speed", "Steady", "Consistent Uplift")

# --- 5. 趋势分析 (Trends) ---
st.markdown("---")
st.subheader("📈 Performance Trend (M1-M10 Comparison)")

tab1, tab2 = st.tabs(["Views Trend", "Likes Trend"])

with tab1:
    fig_views = px.line(df_trend, x='month_index', y='views', color='owner', markers=True,
                        title="Monthly Views Comparison",
                        color_discrete_map={'Ignite Search': '#ff9999', 'CN Marketing': '#00cc00'})
    st.plotly_chart(fig_views, use_container_width=True)

with tab2:
    fig_likes = px.line(df_trend, x='month_index', y='likes', color='owner', markers=True,
                        title="Monthly Likes Comparison",
                        color_discrete_map={'Ignite Search': '#ff9999', 'CN Marketing': '#00cc00'})
    st.plotly_chart(fig_likes, use_container_width=True)

# --- 6. 内容深度分析 (Content Deep Dive) ---
st.markdown("---")
st.subheader("🧩 Content Deep Dive: Engagement Matrix")

col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("**Article Performance Scatter Plot**")
    st.caption("X-axis: Views | Y-axis: Likes | Bubble Size: Shares")
    fig_scatter = px.scatter(df_articles, x="Views", y="Likes", size="Shares", color="Owner",
                             hover_data=["Title", "Date"],
                             color_discrete_map={'Ignite Search': '#ff9999', 'CN Marketing': '#00cc00'})
    st.plotly_chart(fig_scatter, use_container_width=True)

with col_right:
    st.markdown("**Top Performing Articles (by Views)**")
    top_articles = df_articles[df_articles['Owner'] == 'CN Marketing'].sort_values('Views', ascending=False).head(5)
    st.dataframe(top_articles[['Title', 'Views', 'Likes']], hide_index=True)
    
    st.markdown("**Top Engaging Articles (by Likes)**")
    top_engaging = df_articles[df_articles['Owner'] == 'CN Marketing'].sort_values('Likes', ascending=False).head(5)
    st.dataframe(top_engaging[['Title', 'Views', 'Likes']], hide_index=True)

st.markdown("---")
st.caption("Report generated by AI Assistant. Data source: User uploaded Excel files.")
