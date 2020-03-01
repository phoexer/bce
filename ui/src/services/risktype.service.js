// import config from 'config';
import { authHeader } from "../helpers";
import userService from "./user.service";

const apiUrl = process.env.VUE_APP_BASE_URI;

export const riskTypeService = {
  createRiskType,
  createRisk,
  getAll
};

function createRiskType(data) {
  const requestOptions = {
    method: "POST",
    headers: authHeader(),
    body: JSON.stringify(data)
  };

  return fetch(`${apiUrl}/risk-types/`, requestOptions);
}

function createRisk(data) {
  const requestOptions = {
    method: "POST",
    headers: authHeader(),
    body: JSON.stringify(data)
  };

  return fetch(`${apiUrl}/risks/`, requestOptions);
}

function getAll() {
  const requestOptions = {
    method: "GET",
    headers: authHeader()
  };

  return fetch(`${apiUrl}/risk-types/`, requestOptions).then(handleResponse);
}

function handleResponse(response) {
  return response.text().then(text => {
    const data = text && JSON.parse(text);
    if (!response.ok) {
      if (response.status === 401) {
        // auto logout if 401 response returned from api
        userService.logout();
        location.reload(true);
      }

      const error = (data && data.message) || response.statusText;
      return Promise.reject(error);
    }

    return data;
  });
}

export default riskTypeService;
