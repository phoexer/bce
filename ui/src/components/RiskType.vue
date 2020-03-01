<template>
  <div class="row">
    <div class="col-md-12">
      <h2>Create Risk Type</h2>
    </div>
    <div class="col-md-12">
      <form @submit.prevent="submit">
        <div class="form-group">
          <label>Name</label>
          <input
            class="form-control"
            required
            name="name"
            v-model="model['name']"
          />
        </div>
        <div class="form-group">
          <label>Label</label>
          <input
            class="form-control"
            required
            name="label"
            v-model="model['label']"
          />
        </div>
        <div class="form-group">
          <label>Description</label>
          <textarea
            class="form-control"
            name="description"
            v-model="model['description']"
          ></textarea>
        </div>
        <div class="form-group">
          <label>Tool Tips</label>
          <input
            class="form-control"
            name="tooltip"
            v-model="model['tooltip']"
          />
        </div>
        <div class="form-group">
          <label class="form-control" for="active">
            <input
              name="active"
              id="active"
              v-model="model['active']"
              type="checkbox"
            />
            Active
          </label>
        </div>

        <h3>Field</h3>
        <div class="row">
          <div
            class="alert alert-success col-sm-6"
            v-for="(field, index) in model['fields']"
            v-bind:key="index"
          >
            <div class="form-group">
              <label>Name</label>
              <input
                class="form-control"
                required
                name="name"
                v-model="field.name"
              />
            </div>
            <div class="form-group">
              <label>Label</label>
              <input
                class="form-control"
                required
                name="label"
                v-model="field.label"
              />
            </div>
            <div class="form-group">
              <label>Tool Tips</label>
              <input
                class="form-control"
                name="tooltip"
                v-model="field.tooltip"
              />
            </div>
            <div class="form-group">
              <label for="type">Field Type</label>
              <select
                class="form-control"
                name="type"
                id="type"
                v-model="field.type"
                v-on:change="changeType(field, index)"
              >
                <option value="TEXT">Text Field</option>
                <option value="TEXTAREA">Text Area</option>
                <option value="EMAIL">Email Address</option>
                <option value="DATE">Date</option>
                <option value="CURRENCY">Currency</option>
                <option value="NUMBER">Number</option>
                <option value="RADIO">Radio Buttons</option>
                <option value="DROPDOWN">Dropdown</option>
              </select>
            </div>
            <div v-if="field.options.length > 0">
              <table class="table">
                <tr>
                  <th><label>Choice</label></th>
                  <th><label>Label</label></th>
                  <th></th>
                </tr>
                <tr v-for="(option, i) in field.options" v-bind:key="i">
                  <td>
                    <input
                      class="form-control"
                      name="choice"
                      v-model="option.choice"
                    />
                  </td>
                  <td>
                    <input
                      class="form-control"
                      name="label"
                      v-model="option.label"
                    />
                  </td>
                  <td>
                    <button
                      class="btn btn-default"
                      type="button"
                      title="Remove Option"
                      v-on:click="removeOption(field, i)"
                    >
                      Remove Option
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>
                    <button
                      class="btn btn-primary"
                      type="button"
                      title="Add Option"
                      v-on:click="addOption(field)"
                    >
                      Add Option
                    </button>
                  </td>
                </tr>
              </table>
            </div>
            <div class="form-group">
              <label class="form-control">
                <input
                  v-model="field.required"
                  type="checkbox"
                  checked="false"
                />
                Required
              </label>
            </div>
            <button
              class="btn btn-default"
              type="button"
              title="Remove Field"
              v-on:click="removeField(index)"
            >
              Remove Field
            </button>
          </div>
        </div>
        <button
          class="btn btn-primary"
          type="button"
          title="Add Field"
          v-on:click="addField()"
        >
          Add Field
        </button>

        <div>
          <hr />
          <button class="btn btn-primary" type="button" v-on:click="submit()">
            Save
          </button>
        </div>
      </form>
    </div>
    <hr />
  </div>
</template>

<script>
import riskTypeService from '@/services/risktype.service'
import { mapActions } from 'vuex'

export default {
  name: 'RiskType',
  data() {
    return {
      riskType: null,
      model: {
        active: true,
        fields: [],
      },
    }
  },
  created: function() {
    this.addField()
  },
  methods: {
    ...mapActions(['success', 'error', 'clear']),
    removeField(index) {
      this.model['fields'].splice(index, 1)
    },
    addField() {
      this.model['fields'].push({
        name: '',
        label: '',
        type: 'TEXT',
        tooltip: '',
        options: [],
        required: false,
      })
    },
    addOption(field) {
      field.options.push({
        choice: '',
        label: '',
      })
    },
    removeOption(field, index) {
      field.options.splice(index, 1)
    },
    changeType(field) {
      if (field.type == 'RADIO' || field.type == 'DROPDOWN') {
        this.addOption(field)
      } else {
        field.options = []
      }
    },
    submit() {
      riskTypeService
        .createRiskType(this.model)
        .then(response => {
          response.text().then(text => {
            this.res = JSON.parse(text)
            // redirect to home
            if (response.status == 200 || response.status == 201) {
              this.$store.dispatch(
                'alert/success',
                'A new Risk Type has been created with reference number: ' +
                  this.res.id
              )
              this.$router.push({
                path: '/',
              })
            } else if (response.status == 400) {
              for (var msg in this.res) {
                this.$store.dispatch('alert/error', msg + ': ' + this.res[msg])
              }
            }
          })
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
}
</script>
