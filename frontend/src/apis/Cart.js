import Api from "./Api";

const END_POINT = 'shopping/carts';
const END_POINT_SHOPS = 'shopping/shops';

export default {
    all() {
        return Api.get(END_POINT);
    },

    store(data) {
        return Api.post(END_POINT, data);
    },

    delete(id) {
        return Api.delete(`${END_POINT}/${id}`);
    },

    deleteAll(id) {
        return Api.put(`${END_POINT_SHOPS}/${id}/purchase`);
    }
}