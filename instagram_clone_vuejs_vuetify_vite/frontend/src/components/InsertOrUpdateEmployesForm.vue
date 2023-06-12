<template>
  <vee-form @submit="submitData" class="veeform">

              <v-row>
                <v-col cols="12" sm="6" md="4">
                  <v-checkbox 
                    label="Active"
                    v-model="Active"
                    type="input"
                    hide-details
                  ></v-checkbox>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-checkbox 
                    label="Administrator"
                    v-model="Administrator"
                    type="input"
                    hide-details
                  ></v-checkbox>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    label="Password*"
                    v-model="Password"
                    type="input"
                    hide-details
                  ></v-text-field>
                  <span v-if="submitClicked && Password == ''" style="color:red;">{{PasswordAlarm}}</span>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    label="Email*"
                    v-model="Email"
                    type="input"
                    hide-details
                  ></v-text-field>
                  <span v-if="submitClicked && Email == ''" style="color:red;">{{EmailAlarm}}</span>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    label="Name*"
                    v-model="Name"
                    type="input"
                    hide-details
                  ></v-text-field>
                  <span v-if="submitClicked && Name == ''" style="color:red;">{{NameAlarm}}</span>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    label="Middle Name"
                    v-model="MiddleName"
                    type="input"
                    hide-details
                  ></v-text-field>
                  <!-- <span v-if="submitClicked && MiddleName == ''" style="color:red;">{{MiddleNameAlarm}}</span> -->
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    label="Last Name*"
                    v-model="LastName"
                    type="input"
                    hide-details
                  ></v-text-field>
                  <span v-if="submitClicked && LastName == ''" style="color:red;">{{LastNameAlarm}}</span>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-select
                    label="Position*"
                    v-model="Position"
                    :items="['Web Developer', 'Leader', 'Driver', 'Supplier']"
                    hide-details
                  ></v-select>
                  <span v-if="submitClicked && !Position.length" style="color:red;">{{PositionAlarm}}</span>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-file-input
                    label="Image*"
                    accept="image/*"
                    v-model="selectedImages"
                  ></v-file-input>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="DateOfBirth"
                    label="Date of Birth"
                    type="date"
                  ></v-text-field>
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
import { toRaw } from 'vue';
import axios from 'axios';

import { useCounterStore } from '@/stores/counter';
import { mapState } from 'pinia'
import { mapActions } from 'pinia'

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
      DateOfBirth: toRaw(this.insertOrUpdateDialogItem).date_of_birth != undefined ? toRaw(this.insertOrUpdateDialogItem).date_of_birth : null,
      Active:toRaw(this.insertOrUpdateDialogItem).active != undefined ? toRaw(this.insertOrUpdateDialogItem).active : false,
      Administrator:toRaw(this.insertOrUpdateDialogItem).administrator != undefined ? toRaw(this.insertOrUpdateDialogItem).administrator : false,
      Email:toRaw(this.insertOrUpdateDialogItem).email != undefined ? toRaw(this.insertOrUpdateDialogItem).email : '',
      Name:toRaw(this.insertOrUpdateDialogItem).name != undefined ? toRaw(this.insertOrUpdateDialogItem).name : '',
      MiddleName:toRaw(this.insertOrUpdateDialogItem).middle_name != undefined ? toRaw(this.insertOrUpdateDialogItem).middle_name : '',
      LastName:toRaw(this.insertOrUpdateDialogItem).last_name != undefined ? toRaw(this.insertOrUpdateDialogItem).last_name : '',
      Position:toRaw(this.insertOrUpdateDialogItem).position != undefined ? toRaw(this.insertOrUpdateDialogItem).position : [],
      Password:toRaw(this.insertOrUpdateDialogItem).password != undefined ? toRaw(this.insertOrUpdateDialogItem).password : '',
      NameAlarm:'Enter user first name!',
      EmailAlarm:'Enter user email!',
      // MiddleNameAlarm:'Enter middle name!',
      LastNameAlarm:'Enter user last name!',
      PositionAlarm:'Enter user position!',
      PasswordAlarm:'Enter user password!',
      submitClicked:false,
      
      selectedImages: [],    


      login_in_submission: false,
      login_show_alert: false,
      login_alert_variant: 'color: white; background-color:#1a1a1a;  border: 1px solid #1a1a1a; box-shadow:0 0 5px rgba(52, 152, 219, .3), 0 0 10px rgba(52, 152, 219, .2), 0 0 15px rgba(52, 152, 219, .1), 0 1px 0 #1a1a1a4',
      login_alert_msg: 'Please wait! Employ is getting inserted.',
    }
  },
  methods:{
    ...mapActions(useCounterStore, ['logout']),

    submitButtonPushed(){
      this.submitClicked = true
    },
    async submitData(values){
      if(this.Position && this.Name && this.DateOfBirth && this.LastName && this.Email && this.Password){

        this.login_in_submission = true;
        this.login_show_alert = true;

        const formData = new FormData();
        
        for (let i = 0; i < this.selectedImages.length; i++) {
          const file = this.selectedImages[i];
          formData.append('image', file);
        }
        
        formData.append('active', this.Active);
        formData.append('administrator', this.Administrator);
        formData.append('email', this.Email);
        formData.append('name', this.Name);
        formData.append('middle_name', this.MiddleName);
        formData.append('last_name', this.LastName);
        formData.append('position', this.Position);
        formData.append('password', this.Password);
        formData.append('date_of_birth', this.DateOfBirth);
        // console.log(this.Active)
        // console.log(this.Administrator)
        // console.log(this.Email)
        // console.log(this.Name)
        // console.log(this.MiddleName)
        // console.log(this.LastName)
        // console.log(this.Position)
        // console.log(this.Password)
        // console.log(this.DateOfBirth)

        await axios.post(this.BASE_URL+'user/create', formData,
        {
          headers: {
            'Authorization':'Bearer ' + localStorage.getItem('access_token'),
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data' 
          }
        })
          .then(response => {
            // Handle the response from the backend
            console.log('Form submitted successfully', response.data);
            this.login_in_submission = true;
            this.login_alert_variant = 'color: white; background-color:#339933; border: 1px solid #339933; box-shadow: 0 0 5px rgba(0,255,0,.3), 0 0 10px rgba(0,255,0,.2), 0 0 15px rgba(0,255,0,.1), 0 1px 0 #339933;';
            this.login_alert_msg = 'Success! You have inserted new employ.';
          })
          .catch(error => {
            // Handle errors
            console.error('Error submitting form', error);
            if(error.response.data.detail == 'Could not validate credentials'){
              this.logout()          
            }
            this.login_in_submission = true;
            this.login_alert_variant = 'color: white; background-color:#990000;  border: 1px solid #990000;  box-shadow: 0 0 5px rgba(255,0,0,.3), 0 0 10px rgba(255,0,0,.2), 0 0 15px rgba(255,0,0,.1), 0 1px 0 #990000';
            this.login_alert_msg = error.response.data.detail;
            return
          });

          
          setTimeout(()=>{
            window.location.reload();
          },5000)
        // this.login_in_submission = true;
        // this.login_show_alert = true;
        // this.login_alert_variant = 'color: white; background-color:#1a1a1a;  border: 1px solid #1a1a1a; box-shadow:0 0 5px rgba(52, 152, 219, .3), 0 0 10px rgba(52, 152, 219, .2), 0 0 15px rgba(52, 152, 219, .1), 0 1px 0 #1a1a1a4';
        // this.login_alert_msg = 'Please wait! We are logging you in.';

        // values['email'] = this.Email
        // values['name'] = this.Name
        // values['middle_name'] = this.MiddleName
        // values['last_name'] = this.LastName
        // values['administrator'] = this.Administrator
        // values['active'] = this.Active
        // values['position'] = this.Position

        // this.$emit('update:insertOrUpdateItem', values);
        // this.$emit("enter-in-db", values);

        // console.log(values)
      }
      
    }
  },
  created(){
          console.log(toRaw(this.insertOrUpdateDialogItem))

    // console.log(this.insertOrUpdateDialogItem)
  },
  computed: {
    ...mapState(useCounterStore, ['BASE_URL']),

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
    },
    formattedDateOfBirth: {
      get() {
        if (this.DateOfBirth) {
          const date = new Date(this.DateOfBirth);
          const year = date.getFullYear();
          const month = ('0' + (date.getMonth() + 1)).slice(-2); // add leading zero for month
          const day = ('0' + date.getDate()).slice(-2); // add leading zero for day
          return `${year}-${month}-${day}`;
        }
        return null;
      },
      // set(value) {
      //   if (value) {
      //     const parts = value.split('-');
      //     const year = parseInt(parts[0], 10);
      //     const month = parseInt(parts[1], 10) - 1; // subtract 1 from month since it's zero-based
      //     const day = parseInt(parts[2], 10);
      //     const date = new Date(year, month, day);
      //     this.DateOfBirth = date.toISOString().substr(0, 10);
      //   } else {
      //     this.DateOfBirth = null;
      //   }
      // },
    },
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