"""
Test script untuk memverifikasi semua komponen sistem antrian tiket
"""

import sys
from queue_ticket import Queue
from graph_position import Graph
from ticket_system import SistemAntrian, Pembeli

def test_queue():
    """Test Queue implementation"""
    print("=" * 50)
    print("🧪 TEST QUEUE")
    print("=" * 50)
    
    queue = Queue()
    
    # Test enqueue
    print("\n✓ Testing enqueue...")
    pembeli1 = Pembeli(1, "Budi", 30, 40, 1000)
    pembeli2 = Pembeli(2, "Ani", 60, 60, 1001)
    pembeli3 = Pembeli(3, "Citra", 45, 45, 1002)
    
    queue.enqueue(pembeli1)
    queue.enqueue(pembeli2)
    queue.enqueue(pembeli3)
    
    print(f"  Size after enqueue: {queue.get_size()}")
    assert queue.get_size() == 3, "Queue size should be 3"
    print("  ✅ Enqueue test passed!")
    
    # Test peek
    print("\n✓ Testing peek...")
    front = queue.peek()
    print(f"  Front: {front.nama}")
    assert front.nama == "Budi", "Front should be Budi"
    assert queue.get_size() == 3, "Size should not change after peek"
    print("  ✅ Peek test passed!")
    
    # Test dequeue
    print("\n✓ Testing dequeue...")
    dequeued = queue.dequeue()
    print(f"  Dequeued: {dequeued.nama}")
    assert dequeued.nama == "Budi", "Dequeued should be Budi"
    assert queue.get_size() == 2, "Queue size should be 2"
    print("  ✅ Dequeue test passed!")
    
    print("\n✅ All Queue tests passed!\n")


def test_graph():
    """Test Graph implementation"""
    print("=" * 50)
    print("🧪 TEST GRAPH")
    print("=" * 50)
    
    graph = Graph()
    
    # Test add node
    print("\n✓ Testing add_node...")
    graph.add_node(0, 50, 50, "Pusat Penjualan")
    graph.add_node(1, 30, 40, "Budi")
    graph.add_node(2, 60, 60, "Ani")
    graph.add_node(3, 45, 45, "Citra")
    
    print(f"  Total nodes: {len(graph.nodes)}")
    assert len(graph.nodes) == 4, "Should have 4 nodes"
    print("  ✅ Add node test passed!")
    
    # Test set center
    print("\n✓ Testing set_center...")
    graph.set_center(0)
    print(f"  Center: {graph.center.name}")
    assert graph.center.id == 0, "Center should be node 0"
    print("  ✅ Set center test passed!")
    
    # Test add edge
    print("\n✓ Testing add_edge...")
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    
    print(f"  Total edges: {len(graph.edges)}")
    assert len(graph.edges) == 3, "Should have 3 edges"
    print("  ✅ Add edge test passed!")
    
    # Test calculate distance
    print("\n✓ Testing calculate_distance...")
    dist = graph.calculate_distance(1, 3)
    print(f"  Distance between Budi and Citra: {dist}m")
    print("  ✅ Distance calculation test passed!")
    
    # Test get nearest nodes
    print("\n✓ Testing get_nearest_nodes...")
    nearest = graph.get_nearest_nodes(top_n=2)
    print(f"  2 Nearest nodes from center:")
    for node_id, name, distance in nearest:
        print(f"    - {name}: {distance}m")
    print("  ✅ Get nearest nodes test passed!")
    
    print("\n✅ All Graph tests passed!\n")


def test_sistem_antrian():
    """Test SistemAntrian integration"""
    print("=" * 50)
    print("🧪 TEST SISTEM ANTRIAN TERINTEGRASI")
    print("=" * 50)
    
    sistem = SistemAntrian(pusat_x=50, pusat_y=50)
    
    # Test tambah pembeli
    print("\n✓ Testing tambah_pembeli...")
    pembeli1 = sistem.tambah_pembeli("Budi", 30, 40)
    pembeli2 = sistem.tambah_pembeli("Ani", 60, 60)
    pembeli3 = sistem.tambah_pembeli("Citra", 45, 45)
    
    print(f"  Total pembeli: {sistem.jumlah_antrian()}")
    assert sistem.jumlah_antrian() == 3, "Should have 3 pembeli"
    print(f"  Nomor tiket: {pembeli1.nomor_tiket}, {pembeli2.nomor_tiket}, {pembeli3.nomor_tiket}")
    print("  ✅ Tambah pembeli test passed!")
    
    # Test lihat pembeli depan
    print("\n✓ Testing lihat_pembeli_depan...")
    depan = sistem.lihat_pembeli_depan()
    print(f"  Pembeli depan: {depan.nama} (Tiket: {depan.nomor_tiket})")
    assert depan.nama == "Budi", "Front should be Budi"
    print("  ✅ Lihat pembeli depan test passed!")
    
    # Test get prioritas berdasarkan lokasi
    print("\n✓ Testing get_prioritas_berdasarkan_lokasi...")
    prioritas = sistem.get_prioritas_berdasarkan_lokasi()
    print(f"  Urutan prioritas:")
    for p in prioritas:
        print(f"    #{p['priority']}: {p['name']} - {p['distance']}m")
    print("  ✅ Get prioritas test passed!")
    
    # Test get pembeli terdekat
    print("\n✓ Testing get_pembeli_terdekat...")
    terdekat = sistem.get_pembeli_terdekat(2)
    print(f"  2 Pembeli terdekat:")
    for t in terdekat:
        print(f"    - {t['nama']}: {t['jarak']}m")
    print("  ✅ Get pembeli terdekat test passed!")
    
    # Test statistik
    print("\n✓ Testing get_statistik...")
    stat = sistem.get_statistik()
    print(f"  Total pembeli: {stat['total_pembeli']}")
    print(f"  Menunggu: {stat['menunggu']}")
    print(f"  Selesai: {stat['selesai']}")
    print(f"  Progress: {stat['persentase_selesai']:.1f}%")
    print("  ✅ Get statistik test passed!")
    
    # Test lanjutkan pembeli
    print("\n✓ Testing lanjutkan_pembeli...")
    selesai = sistem.lanjutkan_pembeli()
    print(f"  Pembeli selesai: {selesai.nama}")
    assert selesai.nama == "Budi", "Selesai should be Budi"
    assert sistem.jumlah_antrian() == 2, "Queue size should be 2"
    print("  ✅ Lanjutkan pembeli test passed!")
    
    # Test statistik after dequeue
    print("\n✓ Testing statistik after dequeue...")
    stat = sistem.get_statistik()
    print(f"  Menunggu: {stat['menunggu']}")
    print(f"  Selesai: {stat['selesai']}")
    assert stat['selesai'] == 1, "Should have 1 pembeli selesai"
    print("  ✅ Statistik after dequeue test passed!")
    
    print("\n✅ All Sistem Antrian tests passed!\n")


def main():
    """Run all tests"""
    print("\n")
    print("╔" + "═" * 48 + "╗")
    print("║" + " " * 48 + "║")
    print("║" + "🎪 TEST SISTEM ANTRIAN TIKET KEREN 🎪".center(48) + "║")
    print("║" + " " * 48 + "║")
    print("╚" + "═" * 48 + "╝")
    
    try:
        test_queue()
        test_graph()
        test_sistem_antrian()
        
        print("\n╔" + "═" * 48 + "╗")
        print("║" + " " * 48 + "║")
        print("║" + "🎉 ALL TESTS PASSED! 🎉".center(48) + "║")
        print("║" + " " * 48 + "║")
        print("╚" + "═" * 48 + "╝\n")
        
        return 0
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
