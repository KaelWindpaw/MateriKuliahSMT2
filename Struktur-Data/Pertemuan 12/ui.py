import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from graf import Graf

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Google Maps Dynamic Simulator", layout="wide")

# Menggunakan session_state agar objek Graph tetap bertahan saat UI berinteraksi
if 'google_maps' not in st.session_state:
    # Inisialisasi Graph pertama kali
    st.session_state.google_maps = Graf()
    
    # Seeder: Data Awal agar peta tidak kosong saat pertama dibuka
    g = st.session_state.google_maps
    for v in ["Kampus UIN", "Stasiun", "Mall"]: g.add_vertex(v)
    g.add_edge("Kampus UIN", "Stasiun", 5)
    g.add_edge("Stasiun", "Mall", 3)

# Referensi ke objek graph di session state
map_engine = st.session_state.google_maps

st.title("🗺️ Google Maps Simulator (Dynamic Graph)")
st.markdown("Implementasi **Weighted Graph** & **Algoritma Dijkstra** untuk optimasi rute.")

# --- SIDEBAR: INPUT DINAMIS ---
with st.sidebar:
    st.header("📍 Manajemen Vertex (Lokasi)")
    with st.form("form_vertex"):
        new_vertex = st.text_input("Nama Lokasi Baru:")
        submit_v = st.form_submit_button("Tambah Lokasi")
        if submit_v and new_vertex:
            if map_engine.add_vertex(new_vertex):
                st.success(f"Vertex '{new_vertex}' berhasil ditambahkan.")
                st.rerun()
            else:
                st.warning("Vertex sudah terdaftar.")

    st.markdown("---")
    
    st.header("🛣️ Manajemen Edge (Jalan)")
    vertices = map_engine.get_all_vertex()
    
    if len(vertices) >= 2:
        with st.form("form_edge"):
            u = st.selectbox("Titik A:", vertices)
            v = st.selectbox("Titik B:", vertices)
            w = st.number_input("Jarak (KM):", min_value=1, value=1)
            submit_e = st.form_submit_button("Hubungkan Jalan")
            
            if submit_e:
                if u != v:
                    map_engine.add_edge(u, v, w)
                    st.success(f"Edge {u}-{v} ({w}KM) ditambahkan.")
                    st.rerun()
                else:
                    st.error("Titik asal dan tujuan tidak boleh sama.")
    else:
        st.info("Tambahkan minimal 2 lokasi untuk membuat jalan.")

# --- MAIN PAGE: VISUALISASI & ANALISIS ---
col_map, col_nav = st.columns([2, 1])

with col_map:
    st.subheader("🌐 Visualisasi Jaringan (Real-time)")
    
    # Mengonversi Data User-Defined ke NetworkX untuk Penggambaran
    G = nx.Graph()
    for vertex in map_engine.get_all_vertex():
        G.add_node(vertex)
    
    for u, v, w in map_engine.get_all_vertex_with_weight():
        G.add_edge(u, v, weight=w)
    
    if len(G.nodes) > 0:
        fig, ax = plt.subplots(figsize=(10, 8))
        # Gunakan Spring Layout agar node menyebar secara dinamis
        pos = nx.spring_layout(G, seed=10)
        
        # Gambar Node & Label
        nx.draw(G, pos, with_labels=True, node_color="#3b82f6", node_size=2500, 
                font_size=10, font_color="white", font_weight="bold", 
                edge_color="#94a3b8", width=2, ax=ax)
        
        # Gambar Bobot (Jarak) pada Garis
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, ax=ax)
        
        st.pyplot(fig)
    else:
        st.warning("Belum ada data visualisasi.")

with col_nav:
    st.subheader("🚗 Navigasi Dijkstra")
    if len(vertices) >= 2:
        start_node = st.selectbox("Titik Awal:", vertices, key="start")
        end_node = st.selectbox("Titik Tujuan:", vertices, key="end")
        
        if st.button("Cari Rute Terpendek", type="primary", use_container_width=True):
            path, cost = map_engine.find_shortest_path(start_node, end_node)
            
            if path:
                st.success("Rute Terbaik Ditemukan!")
                st.markdown(f"### 🏁 Jalur: \n**{' ➡️ '.join(path)}**")
                st.metric("Total Jarak", f"{cost} KM")
            else:
                st.error("Tidak ada jalur yang menghubungkan kedua lokasi.")
    else:
        st.info("Input minimal 2 lokasi untuk simulasi navigasi.")

# --- FOOTER: DEBUGGING DATA ---
with st.expander("📝 Log Struktur Data (Adjacency List)"):
    st.write(map_engine.adj_list)
