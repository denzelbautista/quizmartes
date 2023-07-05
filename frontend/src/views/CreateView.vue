<template>
  <div class="convoc-creation-form">
    <h1>Registrar Convocatoria</h1>
    <div>
      <form @submit.prevent.stop="registerConvocEvent">
        <div>
          <label>Jugador:</label>
          <input type="text" v-model="convocatoria.jugador" />
        </div>
        <div>
          <label>Equipo:</label>
          <input type="text" v-model="convocatoria.equipo" />
        </div>
        <div>
          <label>Torneo:</label>
          <input type="text" v-model="convocatoria.torneo" />
        </div>
        <button class="submit-button" type="submit">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
import { registerConvoc } from "@/services/convocatoria.api";
export default {
  name: "RegisterConvoc",
  data() {
    return {
      convocatoria: {
        jugador: "",
        equipo: "",
        torneo: "",
      },
    };
  },
  methods: {
    async registerConvocEvent() {
      await registerConvoc(this.convocatoria);
    },
  },
};
</script>

<style>
label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input[type="text"] {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 300px;
}

.submit-button {
  margin-top: 20px;
  background-color: #4caf50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
