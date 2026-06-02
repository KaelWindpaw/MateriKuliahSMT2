"""
Aplikasi Streamlit untuk Sistem Antrian Tiket
Dengan login admin/user, pembelian tiket, top-up saldo, dan visualisasi lokasi.
"""

import streamlit as st
import plotly.graph_objects as go
import random
from ticket_system import SistemAntrian


st.set_page_config(
    page_title="🎟️ Sistem Antrian Tiket Keren",
    page_icon="🎪",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    .stMetric {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00D9FF;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #00D9FF, #0099FF);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 10px;
        transition: transform 0.2s;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.8);
    }
    .header-title {
        text-align: center;
        font-size: 3em;
        background: linear-gradient(90deg, #00D9FF, #0099FF, #FF006E);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: bold;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .info-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #00D9FF;
        margin: 10px 0;
    }
    .status-badge {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        margin: 5px;
    }
    .status-waiting {
        background-color: #FFA500;
        color: white;
    }
    .status-done {
        background-color: #00FF00;
        color: black;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-top: 10px;
    }
    .chat-bubble {
        padding: 18px;
        border-radius: 20px;
        max-width: 72%;
        line-height: 1.5;
        white-space: pre-wrap;
        word-wrap: break-word;
        margin-bottom: 8px;
    }
    .chat-user {
        background: #0099ff;
        color: white;
        margin-left: auto;
        text-align: right;
    }
    .chat-admin {
        background: rgba(255, 255, 255, 0.18);
        color: white;
        margin-right: auto;
        text-align: left;
    }
    .chat-user p,
    .chat-admin p {
        margin: 5px 0 0;
        padding: 0;
    }
    .chat-meta {
        font-size: 0.8rem;
        color: #bbb;
        margin-top: 6px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'sistem' not in st.session_state:
    st.session_state.sistem = SistemAntrian(pusat_x=50, pusat_y=50)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_role = None
    st.session_state.username = None
    st.session_state.full_name = None

if 'menu' not in st.session_state:
    st.session_state.menu = "🔐 Login"

if 'menu_redirect' not in st.session_state:
    st.session_state.menu_redirect = None


def login_section():
    st.markdown("### 🔐 Login Akun")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Masuk", use_container_width=True):
        username = username.strip()
        if not username or not password:
            st.error("Masukkan username dan password.")
            return
        role = st.session_state.sistem.authenticate(username, password)
        if role:
            st.session_state.logged_in = True
            st.session_state.user_role = role
            st.session_state.username = username
            user_info = st.session_state.sistem.get_user_info(username)
            st.session_state.full_name = user_info["name"] if user_info else username
            st.session_state.menu_redirect = "🏠 Dashboard Admin" if role == "admin" else "🏠 Dashboard"
            st.success(f"Selamat datang, {st.session_state.full_name}! Role: {role}")
        else:
            st.error("Username atau password salah.")


def register_section():
    st.markdown("### 📝 Registrasi Akun User")
    username = st.text_input("Username baru", key="register_username")
    password = st.text_input("Password baru", type="password", key="register_password")
    name = st.text_input("Nama lengkap", key="register_name")
    saldo = st.number_input("Saldo awal", min_value=0, value=50000, step=10000, key="register_saldo")
    if st.button("Daftar Akun", use_container_width=True):
        username = username.strip()
        name = name.strip()
        if username and password and name:
            result = st.session_state.sistem.register_user(username, password, name, saldo)
            if result:
                st.success("Akun berhasil dibuat! Silakan login.")
            else:
                st.error("Username sudah terpakai atau data tidak lengkap. Silakan coba lagi.")
        else:
            st.error("Lengkapi semua form registrasi.")


def logout():
    st.session_state.logged_in = False
    st.session_state.user_role = None
    st.session_state.username = None
    st.session_state.full_name = None
    st.success("Anda telah logout.")


def handle_user_chat_submit(username):
    message = st.session_state.user_chat_input.strip()
    if message:
        st.session_state.sistem.send_user_message(username, message)
        st.session_state.sistem.reload_data()
        st.session_state.user_chat_submit_status = "sent"
        st.session_state.user_chat_input = ""
    else:
        st.session_state.user_chat_submit_status = "error"


def handle_admin_chat_submit(chat_id):
    reply = st.session_state.admin_chat_reply.strip()
    if reply:
        st.session_state.sistem.send_admin_message(chat_id, reply)
        st.session_state.sistem.reload_data()
        st.session_state.admin_chat_submit_status = "sent"
        st.session_state.admin_chat_reply = ""
    else:
        st.session_state.admin_chat_submit_status = "error"


def render_user_dashboard():
    username = st.session_state.username
    user = st.session_state.sistem.get_user_info(username)
    st.markdown(f"### 🏠 Dashboard User - {user['name']}")
    if st.button("🔄 Segarkan Data", use_container_width=True, key="user_refresh_dashboard"):
        st.session_state.sistem.reload_data()
        st.success("Data berhasil disegarkan.")

    stats = st.session_state.sistem.get_statistik()
    order_history = st.session_state.sistem.get_user_purchase_history(username)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Saldo", f"Rp {user['saldo']:,}")
    col2.metric("🎫 Tiket Dibeli", len(order_history))
    col3.metric("📍 Posisi Anda", f"({user['location_x']}, {user['location_y']})")

    st.markdown("---")
    st.markdown("### 🛍️ Riwayat Pembelian Tiket")
    if order_history:
        for order in reversed(order_history[-10:]):
            queue_info = f"<p><b>Antrian ke:</b> {order['queue_position']}</p>" if order.get('queue_position') else ""
            status_label = order.get('status_label', order['status'])
            st.markdown(f"""
            <div class="info-box">
            <h4>🎫 {order['ticket_number']} - {order['category']}</h4>
            <p><b>Harga:</b> Rp {order['price']:,}</p>
            <p><b>Status:</b> {status_label}</p>
            {queue_info}
            <p><b>Waktu Pembelian:</b> {order['purchase_time']}</p>
            <p><b>Lokasi:</b> ({order['lokasi_x']}, {order['lokasi_y']})</p>
            """ + (f"<p><b>Served by:</b> {order['served_by']} pada {order['served_time']}</p>" if order['status'] == 'Selesai' else "") + "</div>", unsafe_allow_html=True)
    else:
        st.info("Belum ada pembelian tiket.")


def render_user_buy_ticket():
    username = st.session_state.username
    user = st.session_state.sistem.get_user_info(username)
    st.markdown("### 🎟️ Beli Tiket")
    categories = st.session_state.sistem.get_categories()
    category_names = [cat['name'] for cat in categories]
    
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("Pilih kategori tiket", category_names)
        amount = next((cat['price'] for cat in categories if cat['name'] == category), 0)
        st.write(f"Harga tiket: Rp {amount:,}")
        lokasi_x = st.number_input("Posisi X Anda", min_value=0, max_value=100, value=user['location_x'])
        lokasi_y = st.number_input("Posisi Y Anda", min_value=0, max_value=100, value=user['location_y'])
    with col2:
        st.markdown("### Info User")
        st.write(f"Nama: {user['name']}")
        st.write(f"Username: {user['username']}")
        st.write(f"Saldo: Rp {user['saldo']:,}")
        st.write(f"Posisi: ({user['location_x']}, {user['location_y']})")
    
    if st.button("✅ Beli Tiket", use_container_width=True, key="buy_ticket"):
        order = st.session_state.sistem.purchase_ticket(username, category, lokasi_x, lokasi_y)
        if order:
            st.session_state.sistem.reload_data()
            user = st.session_state.sistem.get_user_info(username)
            position = st.session_state.sistem.get_queue_position(order.ticket_number)
            st.success(f"Tiket berhasil dibeli! Nomor tiket: {order.ticket_number}. Antrian ke: {position}")
            st.write(f"Saldo sekarang: Rp {user['saldo']:,}")
            st.balloons()
        else:
            st.error("Saldo tidak cukup atau kategori tidak valid.")


def render_user_topup():
    username = st.session_state.username
    st.markdown("### 💳 Top Up Saldo")
    amount = st.number_input("Jumlah top up (Rp)", min_value=0, step=10000)
    if st.button("Top Up Sekarang", use_container_width=True):
        if amount > 0:
            st.session_state.sistem.top_up_balance(username, amount)
            st.success(f"Saldo berhasil ditambah Rp {amount:,}")
        else:
            st.error("Masukkan nominal top up yang valid.")


def render_user_location():
    username = st.session_state.username
    user = st.session_state.sistem.get_user_info(username)
    st.markdown("### 📍 Lokasi Pembeli")
    st.write("Atur posisi Anda dan lihat visualisasi semua pembeli.")
    
    col1, col2 = st.columns(2)
    with col1:
        lokasi_x = st.number_input("Lokasi X", min_value=0, max_value=100, value=user['location_x'])
        lokasi_y = st.number_input("Lokasi Y", min_value=0, max_value=100, value=user['location_y'])
        if st.button("Simpan Lokasi", use_container_width=True):
            st.session_state.sistem.set_user_location(username, lokasi_x, lokasi_y)
            st.success("Lokasi Anda berhasil diperbarui.")
    with col2:
        st.write(f"Lokasi saat ini: ({user['location_x']}, {user['location_y']})")
        st.write("Gunakan posisi ini saat membeli tiket.")
    
    render_location_visualization()


def render_user_history():
    username = st.session_state.username
    st.markdown("### 📋 Riwayat Pembelian")
    if st.button("🔄 Segarkan Riwayat", use_container_width=True, key="user_refresh_history"):
        st.session_state.sistem.reload_data()
        st.success("Riwayat berhasil disegarkan.")
    history = st.session_state.sistem.get_user_purchase_history(username)
    if history:
        for order in reversed(history[-10:]):
            queue_info = f"<p><b>Antrian ke:</b> {order['queue_position']}</p>" if order.get('queue_position') else ""
            status_label = order.get('status_label', order['status'])
            st.markdown(f"""
            <div class="info-box">
            <h4>🎫 {order['ticket_number']} - {order['category']}</h4>
            <p><b>Harga:</b> Rp {order['price']:,}</p>
            <p><b>Status:</b> {status_label}</p>
            {queue_info}
            <p><b>Lokasi:</b> ({order['lokasi_x']}, {order['lokasi_y']})</p>
            <p><b>Waktu:</b> {order['purchase_time']}</p>
            {f"<p><b>Served by:</b> {order['served_by']} pada {order['served_time']}</p>" if order['status'] == 'Selesai' else ''}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Belum ada riwayat pembelian.")


def render_user_chat():
    username = st.session_state.username
    st.markdown("### 💬 Chat dengan Admin")
    if st.button("🔄 Segarkan Chat", use_container_width=True, key="user_refresh_chat"):
        st.session_state.sistem.reload_data()
        st.success("Chat berhasil disegarkan.")

    if "user_chat_input" not in st.session_state:
        st.session_state.user_chat_input = ""
    if "user_chat_submit_status" not in st.session_state:
        st.session_state.user_chat_submit_status = None

    if st.session_state.user_chat_submit_status == "sent":
        st.success("Pesan terkirim ke admin.")
        st.session_state.user_chat_submit_status = None
    elif st.session_state.user_chat_submit_status == "error":
        st.error("Masukkan pesan terlebih dahulu.")
        st.session_state.user_chat_submit_status = None

    chat = st.session_state.sistem.get_user_chat(username)
    if chat:
        status = chat.get('status', 'Menunggu')
        position = st.session_state.sistem.get_chat_queue_position(chat['chat_id'])
        if status == 'Menunggu' and position is not None:
            st.info(f"Chat Anda saat ini berada di antrian ke {position} untuk direspon oleh admin.")
        st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
        for message in chat.get('messages', []):
            bubble_class = 'chat-user' if message['sender'] == username else 'chat-admin'
            sender_label = 'Anda' if message['sender'] == username else 'Admin'
            st.markdown(f"<div class='chat-bubble {bubble_class}'><strong>{sender_label}</strong><p>{message['text']}</p><div class='chat-meta'>{message['timestamp']}</div></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Belum ada chat dengan admin. Kirim pesan pertama untuk memulai.")

    st.text_area("Tulis pesan untuk admin", key="user_chat_input", height=140)
    st.button("Kirim Pesan", use_container_width=True, key="user_send_chat", on_click=handle_user_chat_submit, args=(username,))


def render_user_account():
    username = st.session_state.username
    user = st.session_state.sistem.get_user_info(username)
    st.markdown("### ⚙️ Informasi Akun")
    st.write(f"Nama: {user['name']}")
    st.write(f"Username: {user['username']}")
    st.write(f"Saldo: Rp {user['saldo']:,}")
    st.write(f"Posisi: ({user['location_x']}, {user['location_y']})")
    st.markdown("---")
    new_name = st.text_input("Ubah Nama", value=user['name'])
    if st.button("Simpan Nama Baru", use_container_width=True):
        if new_name and new_name != user['name']:
            st.session_state.sistem.update_user_name(username, new_name)
            st.success("Nama berhasil diperbarui.")
        else:
            st.error("Masukkan nama baru yang berbeda.")


def render_admin_dashboard():
    st.markdown("### 🏠 Dashboard Admin")
    if st.button("🔄 Refresh Data", use_container_width=True):
        st.session_state.sistem.reload_data()
        st.success("Data admin berhasil diperbarui.")

    stats = st.session_state.sistem.get_statistik()
    pending_orders = st.session_state.sistem.get_pending_orders()
    order_history = st.session_state.sistem.get_admin_purchase_history()
    pending_chats = st.session_state.sistem.get_pending_chat_count()

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("🕒 Pesanan Menunggu", stats['pending'])
    col2.metric("✅ Pesanan Selesai", stats['completed'])
    col3.metric("💰 Total Pendapatan", f"Rp {stats['revenue']:,}")
    col4.metric("📈 Selesai", f"{stats['completion_rate']:.1f}%")
    col5.metric("💬 Chat Tertunda", pending_chats)
    
    st.markdown("---")
    st.markdown("### 📋 Riwayat Pembelian Tiket")
    if order_history:
        for order in reversed(order_history[-10:]):
            queue_info = f"<p><b>Antrian ke:</b> {order['queue_position']}</p>" if order.get('queue_position') else ""
            status_label = order.get('status_label', order['status'])
            st.markdown(f"""
            <div class="info-box">
            <h4>🎫 {order['ticket_number']} - {order['category']} ({status_label})</h4>
            <p><b>User:</b> {order['username']} - {order['name']}</p>
            <p><b>Harga:</b> Rp {order['price']:,}</p>
            {queue_info}
            <p><b>Lokasi:</b> ({order['lokasi_x']}, {order['lokasi_y']})</p>
            <p><b>Waktu:</b> {order['purchase_time']}</p>
            {f"<p><b>Served by:</b> {order['served_by']} pada {order['served_time']}</p>" if order['status'] == 'Selesai' else ''}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Belum ada pesan tiket.")


def render_admin_serve():
    st.markdown("### 🎫 Melayani Pesanan")
    next_order = st.session_state.sistem.get_next_order()
    if next_order:
        st.markdown(f"#### Pesanan Selanjutnya: {next_order.ticket_number}")
        st.write(f"User: {next_order.username}")
        st.write(f"Nama: {next_order.name}")
        st.write(f"Kategori: {next_order.category}")
        st.write(f"Harga: Rp {next_order.price:,}")
        st.write(f"Lokasi: ({next_order.lokasi_x}, {next_order.lokasi_y})")
        if st.button("✅ Layani Pesanan Ini", use_container_width=True):
            result = st.session_state.sistem.serve_next_order(st.session_state.username)
            if result:
                st.success(f"Pesanan tiket {result.ticket_number} berhasil dilayani.")
    else:
        st.info("Tidak ada pesanan dalam antrean.")

    st.markdown("---")
    pending = st.session_state.sistem.get_pending_orders()
    if pending:
        st.markdown("### 📍 Antrian Tiket (5 Teratas)")
        for idx, order in enumerate(pending[:5], 1):
            st.write(f"{idx}. {order.ticket_number} - {order.name} ({order.category}) - {order.status} - Antrian ke: {idx}")
    else:
        st.info("Tidak ada antrian saat ini.")


def render_admin_categories():
    st.markdown("### 🏷️ Harga Tiket & Kategori")
    categories = st.session_state.sistem.get_categories()
    for category in categories:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write(f"**{category['name']}**")
        with col2:
            new_price = st.number_input(f"Harga {category['name']}", min_value=1000, value=category['price'], step=5000, key=f"cat_{category['name']}")
            if st.button(f"Simpan {category['name']}", key=f"save_{category['name']}"):
                st.session_state.sistem.update_category_price(category['name'], new_price)
                st.success(f"Harga {category['name']} diperbarui.")
    st.markdown("---")
    st.markdown("### ➕ Tambah Kategori Baru")
    name = st.text_input("Nama kategori baru", key="new_category_name")
    price = st.number_input("Harga kategori baru", min_value=1000, value=50000, step=5000, key="new_category_price")
    if st.button("Tambah Kategori", use_container_width=True):
        if name:
            if st.session_state.sistem.add_category(name, price):
                st.success("Kategori baru berhasil ditambahkan.")
            else:
                st.error("Kategori sudah ada.")
        else:
            st.error("Nama kategori tidak boleh kosong.")


def render_admin_user_management():
    st.markdown("### 🧑‍💻 Kelola Akun User")
    users = st.session_state.sistem.db.get_all_users()
    if users:
        user_options = [user['username'] for user in users]
        selected = st.selectbox("Pilih user", user_options)
        user = next((u for u in users if u['username'] == selected), None)
        if user:
            st.write(f"Nama: {user['name']}")
            st.write(f"Saldo: Rp {user['saldo']:,}")
            st.write(f"Posisi: ({user['location_x']}, {user['location_y']})")
            new_name = st.text_input("Ubah nama user", value=user['name'], key="edit_user_name")
            if st.button("Simpan perubahan", use_container_width=True, key="save_user"):
                if new_name and new_name != user['name']:
                    st.session_state.sistem.update_user_name(user['username'], new_name)
                    st.success("Nama user diperbarui.")
                else:
                    st.error("Masukkan nama baru.")
            if st.button("Hapus akun user", use_container_width=True, key="delete_user"):
                st.session_state.sistem.delete_user(user['username'])
                st.success("Akun user dihapus.")
    else:
        st.info("Belum ada user yang terdaftar.")


def render_admin_reset():
    st.markdown("### 🧹 Reset Riwayat & Posisi Pembelian")
    st.warning("Reset data ini akan menghapus semua riwayat pesanan dan mengembalikan posisi pembeli ke nilai default tanpa menghapus akun.")
    confirm_reset = st.checkbox(
        "Saya yakin ingin menghapus semua riwayat pesanan dan mengatur ulang posisi pembeli",
        key="confirm_reset_history"
    )
    if st.button("Reset Semua Riwayat", use_container_width=True, key="admin_reset_history"):
        if not confirm_reset:
            st.error("Centang konfirmasi sebelum melakukan reset.")
        elif st.session_state.sistem.reset_history():
            st.success("Semua riwayat dan posisi pembelian telah direset. Akun tetap tersimpan.")
    st.markdown("---")
    st.markdown("Gunakan fitur ini bila Anda ingin mulai dari ulang tanpa kehilangan data akun atau kategori.")


def render_location_visualization():
    prioritas = st.session_state.sistem.get_prioritas_berdasarkan_lokasi()
    if prioritas:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=[st.session_state.sistem.pusat_x],
            y=[st.session_state.sistem.pusat_y],
            mode='markers+text',
            name='Pusat Penjualan',
            marker=dict(size=30, color='#FF006E', symbol='star'),
            text=['PUSAT'],
            textposition='top center'
        ))
        x_coords = [p['x'] for p in prioritas]
        y_coords = [p['y'] for p in prioritas]
        names = [f"{p['name']} ({p['priority']})" for p in prioritas]
        distances = [p['distance'] for p in prioritas]
        fig.add_trace(go.Scatter(
            x=x_coords,
            y=y_coords,
            mode='markers+text',
            marker=dict(size=15, color=distances, colorscale='Viridis', showscale=True),
            text=names,
            textposition='top center'
        ))
        fig.update_layout(
            title='Visualisasi Posisi Pembeli',
            xaxis=dict(range=[-5, 105]),
            yaxis=dict(range=[-5, 105]),
            template='plotly_dark',
            height=600
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Belum ada data posisi pembeli.")


def render_admin_purchase_graph():
    st.markdown("### 📈 Grafik Pembelian per Tanggal")
    stats = st.session_state.sistem.get_purchase_statistics_by_date()
    if stats:
        dates = [item['date'] for item in stats]
        counts = [item['count'] for item in stats]
        fig = go.Figure(go.Bar(x=dates, y=counts, marker_color='#00D9FF'))
        fig.update_layout(title='Jumlah Pembelian per Tanggal', xaxis_title='Tanggal', yaxis_title='Jumlah Pembelian', template='plotly_dark', height=500)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Belum ada pembelian untuk divisualisasikan.")


def render_admin_chat():
    st.markdown("### 💬 Chat Pengguna")
    if st.button("🔄 Segarkan Chat", use_container_width=True, key="admin_refresh_chat"):
        st.session_state.sistem.reload_data()
        st.success("Chat berhasil disegarkan.")

    if "admin_chat_reply" not in st.session_state:
        st.session_state.admin_chat_reply = ""
    if "admin_chat_submit_status" not in st.session_state:
        st.session_state.admin_chat_submit_status = None

    if st.session_state.admin_chat_submit_status == "sent":
        st.success("Balasan terkirim ke pengguna.")
        st.session_state.admin_chat_submit_status = None
    elif st.session_state.admin_chat_submit_status == "error":
        st.error("Masukkan pesan sebelum mengirim.")
        st.session_state.admin_chat_submit_status = None

    pending_chats = st.session_state.sistem.get_pending_chat_count()
    st.info(f"Ada {pending_chats} chat yang menunggu respon admin.")
    chats = st.session_state.sistem.get_admin_chats()
    if not chats:
        st.info("Belum ada chat dari pengguna.")
        return

    chat_options = [f"{chat['chat_id']} - {chat['username']} ({chat['status']})" for chat in chats]
    selected = st.selectbox("Pilih chat", chat_options, key="admin_chat_select")
    selected_id = int(selected.split(" - ")[0])
    chat = st.session_state.sistem.get_chat_by_id(selected_id)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("#### Daftar Chat")
        for chat_item in chats:
            label = f"{chat_item['username']} - {chat_item['status']}"
            st.write(label)
    with col2:
        if chat:
            st.markdown(f"#### Obrolan dengan {chat['username']}")
            if chat.get('status') == 'Menunggu':
                position = st.session_state.sistem.get_chat_queue_position(chat['chat_id'])
                if position is not None:
                    st.info(f"Chat ini berada di antrian ke {position} untuk dibalas.")
            st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
            for message in chat.get('messages', []):
                bubble_class = 'chat-user' if message['sender'] == chat['username'] else 'chat-admin'
                sender_label = 'User' if message['sender'] == chat['username'] else 'Admin'
                st.markdown(f"<div class='chat-bubble {bubble_class}'><strong>{sender_label}</strong><p>{message['text']}</p><div class='chat-meta'>{message['timestamp']}</div></div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.text_area("Balas chat ini", key="admin_chat_reply", height=140)
            st.button("Kirim Balasan", use_container_width=True, key="admin_send_reply", on_click=handle_admin_chat_submit, args=(chat['chat_id'],))
        else:
            st.info("Chat tidak ditemukan.")


st.markdown('<div class="header-title">🎪 SISTEM ANTRIAN TIKET KEREN 🎪</div>', unsafe_allow_html=True)
st.markdown("---")

with st.sidebar:
    st.markdown("# ⚙️ MENU KONTROL")
    st.markdown("---")
    if st.session_state.menu_redirect:
        st.session_state.menu = st.session_state.menu_redirect
        st.session_state.menu_redirect = None

    if not st.session_state.logged_in:
        options = ["🔐 Login", "📝 Register"]
    elif st.session_state.user_role == "admin":
        pending_chat_count = st.session_state.sistem.get_pending_chat_count()
        chat_label = f"💬 Chat ({pending_chat_count})" if pending_chat_count else "💬 Chat"
        options = ["🏠 Dashboard Admin", "🎫 Melayani Pesanan", "🏷️ Harga Tiket", "🧑‍💻 Kelola User", "🧹 Reset Riwayat", chat_label, "🗺️ Visualisasi Lokasi", "📊 Grafik Pembelian", "📋 Riwayat", "🚪 Logout"]
    else:
        options = ["🏠 Dashboard", "🎫 Beli Tiket", "💳 Top Up", "📍 Lokasi", "💬 Chat Admin", "📋 Riwayat", "⚙️ Akun", "🚪 Logout"]

    if st.session_state.menu not in options:
        st.session_state.menu = options[0]

    menu = st.radio("Menu:", options, key="menu", label_visibility="collapsed")

if not st.session_state.logged_in:
    if menu == "🔐 Login":
        login_section()
    else:
        register_section()
else:
    if menu == "🚪 Logout":
        logout()
    elif st.session_state.user_role == "admin":
        if menu == "🏠 Dashboard Admin":
            render_admin_dashboard()
        elif menu == "🎫 Melayani Pesanan":
            render_admin_serve()
        elif menu == "🏷️ Harga Tiket":
            render_admin_categories()
        elif menu == "🧑‍💻 Kelola User":
            render_admin_user_management()
        elif menu == "🧹 Reset Riwayat":
            render_admin_reset()
        elif menu.startswith("💬 Chat"):
            render_admin_chat()
        elif menu == "🗺️ Visualisasi Lokasi":
            render_location_visualization()
        elif menu == "📊 Grafik Pembelian":
            render_admin_purchase_graph()
        elif menu == "📋 Riwayat":
            st.markdown("### 📋 Riwayat Semua Pembelian")
            render_admin_dashboard()
    else:
        if menu == "🏠 Dashboard":
            render_user_dashboard()
        elif menu == "🎫 Beli Tiket":
            render_user_buy_ticket()
        elif menu == "💳 Top Up":
            render_user_topup()
        elif menu == "📍 Lokasi":
            render_user_location()
        elif menu == "💬 Chat Admin":
            render_user_chat()
        elif menu == "📋 Riwayat":
            render_user_history()
        elif menu == "⚙️ Akun":
            render_user_account()

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888;'>
<p>🎪 <b>Sistem Antrian Tiket Keren</b> 🎪</p>
<p>Implementasi Queue, Graph, dan JSON Database</p>
<p>Powered by Streamlit ✨</p>
</div>
""", unsafe_allow_html=True)
