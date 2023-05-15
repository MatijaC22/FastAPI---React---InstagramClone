<template>
  <vee-form @submit="submitData" class="veeform">

              <v-row>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    label="Reference*"
                    v-model="Reference"
                    type="input"
                    hide-details
                  ></v-text-field>
                  <span v-if="submitClicked && Reference == ''" style="color:red;">{{ReferenceAlarm}}</span>

                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    label="Location*"
                    v-model="Location"
                    type="input"
                    hide-details
                  ></v-text-field>
                  <span v-if="submitClicked && Location == ''" style="color:red;">{{LocationAlarm}}</span>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-select
                    label="Country*"
                    v-model="Country"
                    :items="['Guatemala', 'Mexico', 'Peru', 'Costa Rica']"
                    hide-details
                  ></v-select>
                  <span v-if="submitClicked && !Country.length" style="color:red;">{{CountryAlarm}}</span>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="Responsible Name*"
                    v-model="ResponsableName"
                    type="input"
                    class="mt-4"
                    hide-details
                  ></v-text-field>
                  <span v-if="submitClicked && ResponsableName == ''" style="color:red;">{{LocationAlarm}}</span>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="Client Name*"
                    v-model="ClientName"
                    type="input"
                    hide-details
                  ></v-text-field>
                  <span v-if="submitClicked && ClientName == ''" style="color:red;">{{ClientNameAlarm}}</span>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-select
                    label="Transport Type*"
                    v-model="TransportType"
                    :items="['Air', 'Land', 'Sea']"
                    class="mt-4"
                    hide-details
                  ></v-select>
                  <span v-if="submitClicked && !TransportType.length" style="color:red;">{{TransportTypeAlarm}}</span>
                </v-col>
                <v-col cols="12" sm="6" >
                  <v-autocomplete
                    :items="['Oil', 'Cooking Oil', 'Greese', 'Cleaning liquid']"
                    label="Product Type*"
                    v-model="ProductType"
                    hint="enter type of the product"
                    class="mt-4"
                    multiple
                    hide-details
                  ></v-autocomplete>
                  <span v-if="submitClicked && !ProductType.length" style="color:red;">{{ProductTypeAlarm}}</span>
                </v-col>
              </v-row>
    <v-btn 
      type="submit" 
      block 
      class="mt-10 submit"
      @click="submitButtonPushed"
      :disabled="login_in_submission"
      >
      Submit

    </v-btn>
  </vee-form>

  <br>
  <div v-if="login_show_alert" :style="login_alert_variant" style="text-align:center;">
    {{ login_alert_msg }}
  </div>
</template>

<script>
import { isProxy, toRaw } from 'vue';

export default {
  props:{
    insertOrUpdateDialogItem: {
      type: Object,
      required: true,
    },
    type: {
      type: String,
      required: true,
    }
  },
  data() {
    return{
      // loginSchema: {
      //   ref:'required|min:3|max:32',
      //   location:'required',
      //   ResponsableName: 'required',
      //   clientName: 'required'
      // },
      Reference:toRaw(this.insertOrUpdateDialogItem).Reference != undefined ? toRaw(this.insertOrUpdateDialogItem).Reference : '',
      Location:toRaw(this.insertOrUpdateDialogItem).Location != undefined ? toRaw(this.insertOrUpdateDialogItem).Location : '',
      ResponsableName:toRaw(this.insertOrUpdateDialogItem).ResponsableName != undefined ? toRaw(this.insertOrUpdateDialogItem).ResponsableName : '',
      ClientName:toRaw(this.insertOrUpdateDialogItem).ClientName != undefined ? toRaw(this.insertOrUpdateDialogItem).ClientName : '',
      Country:toRaw(this.insertOrUpdateDialogItem).Country != undefined ? toRaw(this.insertOrUpdateDialogItem).Country : [],
      TransportType:toRaw(this.insertOrUpdateDialogItem).TransportType != undefined ? toRaw(this.insertOrUpdateDialogItem).TransportType : [],
      ProductType:toRaw(this.insertOrUpdateDialogItem).ProductType != undefined ? toRaw(this.insertOrUpdateDialogItem).ProductType : [],
      ReferenceAlarm:'Enter container reference!',
      LocationAlarm:'Enter location!',
      ResponsableNameAlarm:'Enter supervisor name!',
      ClientNameAlarm:'Enter client name!',
      CountryAlarm: 'Choose country!',
      TransportTypeAlarm: 'Choose type of transport!',
      ProductTypeAlarm: 'Choose at least one option!',
      submitClicked:false,

      


      login_in_submission: false,
      login_show_alert: false,
      login_alert_variant: 'color: #c7c7c7;  border: 1px solid #1a1a1a; box-shadow:0 0 5px rgba(52, 152, 219, .3), 0 0 10px rgba(52, 152, 219, .2), 0 0 15px rgba(52, 152, 219, .1), 0 1px 0 black',
      login_alert_msg: 'Please wait! We are logging you in.',
    }
  },
  methods:{
    submitButtonPushed(){
      this.submitClicked = true
    },
    submitData(values){
      if(this.Country.length && this.TransportType.length && this.ProductType.length && this.Reference && this.Location && this.ResponsableName && this.ClientName){
        this.login_in_submission = true;
        this.login_show_alert = true;
        this.login_alert_variant = 'color: white; background-color:#1a1a1a;  border: 1px solid #1a1a1a; box-shadow:0 0 5px rgba(52, 152, 219, .3), 0 0 10px rgba(52, 152, 219, .2), 0 0 15px rgba(52, 152, 219, .1), 0 1px 0 #1a1a1a4';
        this.login_alert_msg = 'Please wait! We are logging you in.';

        values['Country'] = this.Country
        values['TransportType'] = this.TransportType
        values['ProductType'] = this.ProductType
        values['Reference'] = this.Reference
        values['Location'] = this.Location
        values['ResponsableName'] = this.ResponsableName
        values['ClientName'] = this.ClientName

        this.$emit('update:insertOrUpdateItem', values);
        this.$emit("enter-in-db", values);

        console.log(values)
      }
      
    }
  },
  created(){
          console.log(toRaw(this.insertOrUpdateDialogItem))

    console.log(this.insertOrUpdateDialogItem)
  },
  computed: {
    myProxy() {
      console.log(new Proxy(this.insertOrUpdateDialogItem,{}))
      return new Proxy(this.insertOrUpdateDialogItem,{}
      //  {
      //   get(target, key) {
      //     console.log(`Getting ${key} value: ${target[key]}`);
      //     return target[key];
      //   },
      //   set(target, key, value) {
      //     console.log(`Setting ${key} value: ${value}`);
      //     target[key] = value;
      //     return true;
      //   }
      // }
      );
    }
  }
}
</script>


<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');

.text{
  font-size: 30px;
  color: white;
  font-weight: 600;
  letter-spacing: 2px;
  // text-align:center;
}
// .veeform{
//   margin-top: 10px;
// }
.veeform .field{
  margin-top: 20px;
  display: flex;
}
.field .fas{
  height: 50px;
  width: 60px;
  color: #868686;
  font-size: 20px;
  line-height: 50px;
  border-bottom: 1px solid #444;
  border-right: none;
  border-radius: 5px 0 0 5px;
  background: linear-gradient(#333,#222);
}
.field .veeinput,.veeform button{
  height: 50px;
  width: 100%;
  outline: none;
  font-size: 16px;
  color: #bbb;
  padding: 0 15px;
  border-radius: 0 5px 5px 0;
  border-bottom: 1px solid #bbb;
  caret-color: #3399cc;
  // background: linear-gradient(#333,#222);
  // background: linear-gradient(#bbb, #ddd);
  background: linear-gradient(#F8F8F8	, #F8F8F8);
  // background: linear-gradient(#DDD, #BBB);
  // background: linear-gradient(hsl(0, 0%, 50%), hsl(0, 0%, 30%));




}
.veeinput:focus {
  color: #3399cc;
  box-shadow: 0 0 5px rgba(0, 191, 255, 0.2),
              inset 0 0 5px rgba(0, 191, 255, 0.1);
  // background: linear-gradient(#333933, #222922);
  animation: glow .8s ease-out infinite alternate;
}

@keyframes glow {
  0% {
    border-color: #3399cc;
    // box-shadow: 0 0 5px rgba(0, 191, 255, 0.2),
    //             inset 0 0 5px rgba(0, 0, 0, 0.1);
  }
  100% {
    border-color: #99ccff;
    // box-shadow: 0 0 20px rgba(0, 191, 255, 0.6),
    //             inset 0 0 10px rgba(0, 191, 255, 0.4);
  }
}

.submit{
  margin-top: 30px;
  border-radius: 5px!important;
  font-weight: 600;
  letter-spacing: 1px;
  cursor: pointer;
}
.submit:hover{
  color: #3399cc;
  border: 1px solid #3399cc;
  box-shadow: 0 0 5px rgba(0, 191, 255, 0.3),
              0 0 10px rgba(0, 191, 255, 0.2),
              0 0 15px rgba(0, 191, 255, 0.1);
}

</style>