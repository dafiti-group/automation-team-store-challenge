import axios from 'axios';

export const addNotification = ({ commit }, notification) => {
    commit('PUSH_NOTIFICATION', notification);
}

export const removeNotification = ({ commit }, notification) => {
    commit('REMOVE_NOTIFICATION', notification);
}

export const initializeStore = ({ commit }) => {
    commit('INITIALIZE_STORE');
}
export const setIsLoading = ({ commit }, status) => {
    commit('SET_ISLOADING', status);
}
export const setToken = ({ commit }, token) => {
    commit('SET_TOKEN', token);
}
export const removeToken = ({ commit }) => {
    commit('REMOVETOKEN');
}
export const setUser = ({ commit }, user) => {
    commit('SET_USER', user);
}
export const setTeam = ({ commit }, team) => {
    commit('SET_TEAM', team);
}

export const checkUser = async ({ commit, state }, callback) => {
    await axios
      .get('/api/v1/users/me/', {
        headers: {
            Authorization: 'Token ' + state.token
        }})
      .then(response => {
        const user = {"id": response.data.id, "username": response.data.username}

        commit('SET_USER', user);

        if (callback) {
            callback();
        }
      })
      .catch(() => {
        callback();
      })
}