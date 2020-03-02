<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-6">
        <div class="form-group">
          <h2>Create Risk</h2>
          <label for="risk_type_dd">Please select risk type</label>
          <select
            class="form-control"
            id="risk_type_dd"
            required
            v-model="selected"
          >
            <option value="" selected="true" disabled>Select Risk Type</option>
            <option
              v-for="(riskType, index) in riskTypes"
              v-bind:key="index"
              v-bind:value="riskType"
            >
              {{ riskType.label }}
            </option>
          </select>
        </div>
      </div>
    </div>

    <div class="row" v-if="selected && selected.name">
      <div class="col-sm-12">
        <form @submit.prevent="submit">
          <h2>Creating new {{ selected.name }} risk</h2>
          <div v-for="(field, index) in selected.fields" v-bind:key="index">
            <md-field v-if="field.type == 'TEXT'">
              <label>{{ field.label }}</label>
              <md-input
                v-model="models[field.name]"
                :required="field.required"
                :name="field.name"
              >
                <md-tooltip md-direction="right">{{
                  field.tooltip
                }}</md-tooltip>
              </md-input>
            </md-field>

            <md-field v-if="field.type == 'TEXTAREA'">
              <label>{{ field.label }}</label>
              <md-textarea
                v-model="models[field.name]"
                :name="field.name"
                :required="field.required"
              >
                <md-tooltip md-direction="right">{{
                  field.tooltip
                }}</md-tooltip>
              </md-textarea>
            </md-field>

            <md-datepicker
              v-model="models[field.name]"
              v-if="field.type == 'DATE'"
              :name="field.name"
              :required="field.required"
            >
              <label>{{ field.label }}</label>
              <md-tooltip md-direction="right">{{ field.tooltip }}</md-tooltip>
            </md-datepicker>

            <md-field v-if="field.type == 'EMAIL'">
              <label>{{ field.label }}</label>
              <md-input
                type="email"
                v-model="models[field.name]"
                :required="field.required"
                :name="field.name"
              >
                <md-tooltip md-direction="right">{{
                  field.tooltip
                }}</md-tooltip>
              </md-input>
            </md-field>

            <md-field
              v-if="
                field.type == 'NUMBER' ||
                  field.type == 'INTEGER' ||
                  field.type == 'FLOAT' ||
                  field.type == 'CURRENCY'
              "
            >
              <label>{{ field.label }}</label>
              <span v-if="field.type == 'CURRENCY'" class="md-prefix">$</span>
              <md-input
                v-model="models[field.name]"
                type="number"
                :required="field.required"
                :name="field.name"
              >
                <md-tooltip md-direction="right">{{
                  field.tooltip
                }}</md-tooltip>
              </md-input>
            </md-field>

            <div v-if="field.type == 'RADIO'">
              <label>{{ field.label }}</label>
              <br />
              <md-radio
                v-model="models[field.name]"
                v-for="(option, index) in field.options"
                :id="field.name"
                :name="field.name"
                v-bind:key="index"
                :value="option.choice"
              >
                {{ option.label }}
              </md-radio>
            </div>

            <md-field v-if="field.type == 'DROPDOWN'">
              <label>{{ field.label }}</label>
              <md-select
                v-model="models[field.name]"
                :id="field.name"
                :name="field.name"
              >
                <md-option
                  v-for="(option, index) in field.options"
                  v-bind:key="index"
                  :value="option.choice"
                  >{{ option.label }}
                </md-option>
              </md-select>
            </md-field>
          </div>
          <button type="submit" class="btn btn-success">Submit</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import riskTypeService from "@/services/risktype.service";

export default {
  name: "Risk",
  data() {
    return {
      riskTypes: [{}, {}],
      selected: null,
      models: {}
    };
  },
  created: function() {
    this.getAll();
  },
  methods: {
    getAll() {
      riskTypeService.getAll().then(riskTypes => {
        this.riskTypes = riskTypes;
      });
    },
    submit() {
      let model = {};

      model["name"] = this.selected.name;

      model["data"] = btoa(JSON.stringify(this.models));

      riskTypeService
        .createRisk(model)
        .then(response => {
          response.text().then(text => {
            this.res = JSON.parse(text);

            // redirect to home
            if (response.status == 200 || response.status == 201) {
              this.$router.push({
                path: "/"
              });

              this.$store.dispatch(
                "alert/success",
                "A new " +
                  this.res.name +
                  " Risk has been created with reference number: " +
                  this.res.id
              );
            } else if (response.status == 400) {
              for (var msg in this.res) {
                this.$store.dispatch("alert/error", msg + ": " + this.res[msg]);
              }
            }
          });
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>
