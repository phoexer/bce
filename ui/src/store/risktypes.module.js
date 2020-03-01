// import { userService } from '../services';
import { riskTypeService } from "../services";

export const riskTypes = {
  namespaced: true,
  state: {
    all: {},
    riskTypes: ["one"]
  },
  getters: {
    getAllRiskTypes: () => {
      return riskTypeService.getAll();
    }
  },
  actions: {
    getAll({ commit }) {
      commit("getAllRequest");

      riskTypeService.getAll().then(
        riskTypes => commit("getAllSuccess", riskTypes),
        error => commit("getAllFailure", error)
      );
    }
  },
  mutations: {
    createRiskType: (state, data) => {
      return riskTypeService.createRiskType(data);
    },
    getAllTypes: state => {
      state.riskTypes = riskTypeService.getAll();
    },
    getAllRequest(state) {
      state.all = { loading: true };
    },
    getAllSuccess(state, riskTypes) {
      state.all = { items: riskTypes };
    },
    getAllFailure(state, error) {
      state.all = { error };
    }
  }
};
