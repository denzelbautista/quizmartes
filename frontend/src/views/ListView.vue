<template>
  <h1>Lista de Convocados</h1>
  <div class="list-convoc"></div>
  <ul>
    <li v-for="convocatoria in convocatorias" :key="convocatoria.id">
      "{{ convocatoria.jugador }}" juega en el equipo "{{
        convocatoria.equipo
      }}" del torneo "{{ convocatoria.torneo }}"
    </li>
  </ul>
</template>

<script>
import { listConvoc } from "@/services/listconvocatoria.api";
export default {
  name: "ListConvocatorias",
  mounted() {
    this.loadConvoc();
  },
  data() {
    return {
      convocatorias: [],
    };
  },
  methods: {
    async loadConvoc() {
      const { convocatorias } = await listConvoc();
      console.log("convocatoriaslist.vue: ", convocatorias);
      this.convocatorias = convocatorias;
    },
  },
};
</script>

<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

li {
  margin: 10px;
  padding: 10px;
  border-radius: 5px;
}

li:hover {
  background-color: #eee;
}
</style>
