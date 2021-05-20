export const PUSH_NOTIFICATION = (state, notification) => {
    state.notifications.push({
        ...notification,
        id: (Math.random().toString(36) + Date.now().toString(36)).substr(2)
    })
}

export const REMOVE_NOTIFICATION = (state, notificationToRemove) => {
    state.notifications = state.notifications.filter(notification => {
        return notification.id != notificationToRemove.id;
    })
}

export const INITIALIZE_STORE = (state) => {
  if (localStorage.getItem('token')) {
    state.token = localStorage.getItem('token')
    state.isAuthenticated = true
  } else {
    state.token = ''
    state.isAuthenticated = false
    state.user.id = 0
    state.user.username = ''
  }
}

export const SET_ISLOADING = (state, status) => {
  state.isLoading = status
}

export const SET_TOKEN = (state, token) => {
  state.token = token
  state.isAuthenticated = true
}

export const REMOVETOKEN = (state) => {
  state.token = ''
  state.isAuthenticated = false
}

export const SET_USER = (state, user) => {
  state.user = user
}
