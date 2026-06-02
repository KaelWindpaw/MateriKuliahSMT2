import streamlit as st
import graphviz
import importlib
from logic import FileSystemTree

# --- CONFIG ---
st.set_page_config(page_title="File System Tree Visualizer", layout="wide")

if 'fs_tree' not in st.session_state:
    st.session_state.fs_tree = FileSystemTree()
    # Seeder: Data Awal
    st.session_state.fs_tree.add_node("C:", "Users", is_folder=True)
    st.session_state.fs_tree.add_node("Users", "Nahdiya", is_folder=True)
    st.session_state.fs_tree.add_node("Nahdiya", "Documents", is_folder=True)
    st.session_state.fs_tree.add_node("Documents", "tugas.docx", is_folder=False)

fs = st.session_state.fs_tree

st.title("📂 File System Tree Visualizer")
st.markdown("Simulasi Struktur Data **General Tree** pada Hierarki Folder Sistem Operasi.")
st.write("Nama: **Nahdiya Ilmy**")

# --- SIDEBAR: KONTROL ---
with st.sidebar:
    st.header("🏗️ Kelola File System")
    
    parent_list = fs.get_all_folders()
    selected_parent = st.selectbox("Pilih Folder Induk (Parent):", parent_list)
    
    new_name = st.text_input("Nama Baru:")
    item_type = st.radio("Tipe:", ["Folder", "File"])
    
    if st.button("Tambahkan ke Sistem", type="primary"):
        if new_name:
            is_f = True if item_type == "Folder" else False
            if fs.add_node(selected_parent, new_name, is_f):
                st.success(f"'{new_name}' berhasil ditambahkan ke '{selected_parent}'")
                st.rerun()
            else:
                st.error("Gagal menambahkan (Nama duplikat atau Parent tidak valid).")

# --- MAIN CONTENT ---
edges = fs.get_structure()
col_viz, col_log = st.columns([2, 1])

with col_viz:
    st.subheader("🖥️ Visualisasi Struktur Direktori")
    
    dot = graphviz.Digraph()
    dot.attr('node', style='filled', fontname='Helvetica')
    
    # Render Root
    dot.node(fs.root.name, shape='folder', fillcolor='#fef3c7', color='#d97706')
    
    # Render Children
    for parent, child, is_folder in edges:
        if is_folder:
            dot.node(child, shape='folder', fillcolor='#fef3c7', color='#d97706')
        else:
            dot.node(child, shape='note', fillcolor='#f0fdf4', color='#16a34a')
        dot.edge(parent, child)
    
    st.graphviz_chart(dot)

with col_log:
    st.subheader("🔍 Metadata")
    st.write(f"**Root Node:** `{fs.root.name}`")
    st.write(f"**Total Objek:** {len(edges) + 1}")
    
    st.markdown("---")
    st.info("""
    **Penjelasan Struktur:**
    - Ikon Kuning: Folder (Node Internal)
    - Ikon Hijau: File (Leaf Node)
    - Garis: Edge (Hierarki/Path)
    """)