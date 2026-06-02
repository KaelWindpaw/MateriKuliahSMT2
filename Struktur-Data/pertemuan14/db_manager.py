"""
Database manager menggunakan JSON untuk menyimpan akun, kategori tiket, dan orders.
"""

import copy
import json
import os
from datetime import datetime
from typing import Any, Dict, List, Optional


DEFAULT_DB = {
    "admins": [
        {
            "username": "admin",
            "password": "admin123",
            "full_name": "Admin Utama"
        }
    ],
    "users": [],
    "categories": [
        {"name": "Reguler", "price": 50000},
        {"name": "VIP", "price": 100000},
        {"name": "VVIP", "price": 150000}
    ],
    "orders": [],
    "chats": []
}


class DatabaseManager:
    def __init__(self, file_path: Optional[str] = None):
        self.file_path = file_path or os.path.join(os.path.dirname(__file__), "database.json")
        self.data = self._load_database()
    
    def _load_database(self) -> Dict[str, Any]:
        if not os.path.exists(self.file_path):
            self._save_database(DEFAULT_DB)
            return self._normalize_existing_data(copy.deepcopy(DEFAULT_DB))

        try:
            with open(self.file_path, "r", encoding="utf-8") as handle:
                data = json.load(handle)
                return self._normalize_existing_data(data)
        except (json.JSONDecodeError, IOError):
            backup_path = f"{self.file_path}.corrupt.{datetime.now().strftime('%Y%m%d%H%M%S')}"
            try:
                os.rename(self.file_path, backup_path)
            except OSError:
                pass
            self._save_database(DEFAULT_DB)
            return self._normalize_existing_data(copy.deepcopy(DEFAULT_DB))
    
    def _save_database(self, data: Dict[str, Any]) -> None:
        with open(self.file_path, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=4, ensure_ascii=False)
    
    def save(self) -> None:
        self._save_database(self.data)
    
    def _normalize_username(self, username: str) -> str:
        return username.strip()

    def _normalize_existing_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        for user in data.get("users", []):
            if isinstance(user.get("username"), str):
                user["username"] = self._normalize_username(user["username"])
            if isinstance(user.get("name"), str):
                user["name"] = user["name"].strip()
        for order in data.get("orders", []):
            if isinstance(order.get("username"), str):
                order["username"] = self._normalize_username(order["username"])
            if isinstance(order.get("name"), str):
                order["name"] = order["name"].strip()
        for chat in data.get("chats", []):
            if isinstance(chat.get("username"), str):
                chat["username"] = self._normalize_username(chat["username"])
            chat["status"] = chat.get("status", "Menunggu")
            chat["created_at"] = chat.get("created_at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            chat["updated_at"] = chat.get("updated_at", chat["created_at"])
            chat["messages"] = chat.get("messages", [])
            for message in chat["messages"]:
                if isinstance(message.get("sender"), str):
                    message["sender"] = message["sender"].strip()
                message["text"] = message.get("text", "")
                message["timestamp"] = message.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return data

    def get_admin(self, username: str) -> Optional[Dict[str, Any]]:
        username = self._normalize_username(username)
        return next((admin for admin in self.data["admins"] if self._normalize_username(admin["username"]) == username), None)
    
    def get_user(self, username: str) -> Optional[Dict[str, Any]]:
        username = self._normalize_username(username)
        return next((user for user in self.data["users"] if self._normalize_username(user["username"]) == username), None)
    
    def authenticate(self, username: str, password: str) -> Optional[str]:
        if not username or not password:
            return None
        admin = self.get_admin(username)
        if admin and admin["password"] == password:
            return "admin"
        user = self.get_user(username)
        if user and user["password"] == password:
            return "user"
        return None
    
    def register_user(self, username: str, password: str, name: str, saldo: int = 0) -> bool:
        username = self._normalize_username(username)
        name = name.strip()
        if not username or not password or not name:
            return False
        if self.get_user(username) or self.get_admin(username):
            return False
        self.data["users"].append({
            "username": username,
            "password": password,
            "name": name,
            "saldo": saldo,
            "location_x": 50,
            "location_y": 50
        })
        self.save()
        return True
    
    def update_user(self, username: str, **fields: Any) -> bool:
        user = self.get_user(username)
        if not user:
            return False
        for key, value in fields.items():
            if key in ["name", "saldo", "location_x", "location_y", "password"]:
                user[key] = value
        self.save()
        return True
    
    def delete_user(self, username: str) -> bool:
        username = self._normalize_username(username)
        user = self.get_user(username)
        if not user:
            return False
        self.data["users"] = [u for u in self.data["users"] if self._normalize_username(u["username"]) != username]
        self.save()
        return True
    
    def get_categories(self) -> List[Dict[str, Any]]:
        return self.data["categories"]
    
    def add_category(self, name: str, price: int) -> bool:
        if any(cat["name"].lower() == name.lower() for cat in self.data["categories"]):
            return False
        self.data["categories"].append({"name": name, "price": price})
        self.save()
        return True
    
    def update_category(self, name: str, price: int) -> bool:
        for category in self.data["categories"]:
            if category["name"].lower() == name.lower():
                category["price"] = price
                self.save()
                return True
        return False
    
    def remove_category(self, name: str) -> bool:
        categories = [cat for cat in self.data["categories"] if cat["name"].lower() != name.lower()]
        if len(categories) == len(self.data["categories"]):
            return False
        self.data["categories"] = categories
        self.save()
        return True
    
    def get_order(self, ticket_number: int) -> Optional[Dict[str, Any]]:
        return next((order for order in self.data["orders"] if order["ticket_number"] == ticket_number), None)
    
    def add_order(self, order: Dict[str, Any]) -> None:
        self.data["orders"].append(order)
        self.save()
    
    def update_order(self, ticket_number: int, **fields: Any) -> bool:
        order = self.get_order(ticket_number)
        if not order:
            return False
        for key, value in fields.items():
            if key in order:
                order[key] = value
        self.save()
        return True
    
    def get_orders(self, status: Optional[str] = None, username: Optional[str] = None) -> List[Dict[str, Any]]:
        orders = self.data["orders"]
        if status:
            orders = [order for order in orders if order["status"] == status]
        if username:
            username = self._normalize_username(username)
            orders = [order for order in orders if self._normalize_username(order["username"]) == username]
        return sorted(orders, key=lambda x: x["purchase_time"])
    
    def get_purchase_stats_by_date(self) -> List[Dict[str, Any]]:
        counts: Dict[str, int] = {}
        for order in self.data["orders"]:
            date = order["purchase_time"].split(" ")[0]
            counts[date] = counts.get(date, 0) + 1
        return [{"date": d, "count": counts[d]} for d in sorted(counts.keys())]
    
    def get_all_users(self) -> List[Dict[str, Any]]:
        return self.data["users"]
    
    def get_all_orders(self) -> List[Dict[str, Any]]:
        return self.data["orders"]

    def get_chat(self, chat_id: int) -> Optional[Dict[str, Any]]:
        return next((chat for chat in self.data.get("chats", []) if chat.get("chat_id") == chat_id), None)

    def get_chats(self, status: Optional[str] = None, username: Optional[str] = None) -> List[Dict[str, Any]]:
        chats = self.data.get("chats", [])
        if status:
            chats = [chat for chat in chats if chat.get("status") == status]
        if username:
            username = self._normalize_username(username)
            chats = [chat for chat in chats if self._normalize_username(chat.get("username", "")) == username]
        return sorted(chats, key=lambda x: x["created_at"])

    def get_all_chats(self) -> List[Dict[str, Any]]:
        return self.data.get("chats", [])

    def add_chat(self, chat: Dict[str, Any]) -> None:
        self.data.setdefault("chats", []).append(chat)
        self.save()

    def update_chat(self, chat_id: int, **fields: Any) -> bool:
        chat = self.get_chat(chat_id)
        if not chat:
            return False
        for key, value in fields.items():
            if key in ["status", "updated_at", "username"] or key == "messages":
                chat[key] = value
        self.save()
        return True

    def add_chat_message(self, chat_id: int, message: Dict[str, Any]) -> bool:
        chat = self.get_chat(chat_id)
        if not chat:
            return False
        chat.setdefault("messages", []).append(message)
        chat["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save()
        return True

    def reset_orders(self) -> None:
        self.data["orders"] = []
        for user in self.data.get("users", []):
            user["location_x"] = 50
            user["location_y"] = 50
        self.save()
