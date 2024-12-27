# Елена Андреева, 25-я когорта — Финальный проект. Инженер по тестированию плюс

from create_order import create_order, get_order_by_track
import data

def test_create_and_get_order_by_track():
    # Создаем заказ
    order_response = create_order(data.order_body)
    assert order_response.status_code == 201  # Проверка создания заказа

    # Получаем номер заказа
    order_track_number = order_response.json().get("track")
    assert order_track_number is not None  # Проверка получения номера заказа

    # Получаем данные заказа по номеру
    data_order = get_order_by_track(order_track_number)
    assert data_order.status_code == 200  # Проверка получения заказа по номеру заказа