<template>
<v-main>
  <v-container fluid class="pa-1">
    <v-card class="pa-1" elevation="2" style="background-image: linear-gradient(to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)), url('../src/assets/images/background3.jpg'); background-size: cover;">
      <v-row justify="center" style="padding-top:12px;">
        <v-card
          :key="post.id"
          border
          class="mb-4"
          density="compact"
          variant="text"
          style="background-color:white;"
          width="800"
        >
          <v-list-item :title="post.caption" :subtitle="'Ref: ' + post.id" value="Card details">
            <template v-slot:prepend>
              <router-link :to="'/user/' + post.id + '?part=info'" @click="tab=0">
                <v-avatar image="https://randomuser.me/api/portraits/women/10.jpg" :to="'/user/' + post.userId + '?part=info'" size="38" class="mr-4"></v-avatar>
              </router-link>
            </template>
          </v-list-item>
          
          <v-carousel
            cycle
            height="400"
            hide-delimiter-background
            show-arrows="hover"
            
          >
            <v-carousel-item
              v-for="(slide, i) in [post.image_url, post.image_url]"
              :src="post.image_url_type == 'relative' ? 'http://localhost:8000/'+slide : slide"
              :key="i"
              style="object-fit: contain; object-position: center; background-color:black;"
            >
            </v-carousel-item>
          </v-carousel>

          <v-card-text>
            {{post.caption}}
          </v-card-text>

          <v-card border
            density="compact"
            title="Messages"
            variant="text"
            class="mx-2"
            >
            <v-card-text class="overflow-y-auto" style="max-height:500px;">
              <v-timeline density="compact" align="start" >
                <v-timeline-item
                  v-for="comment in comments"
                  :key="comment.timestamp"
                  :dot-color="comment.username ==  username ? 'deep-purple-lighten-1' : 'green'"
                  size="x-small"
                >

                  <div>
                    <div class="mb-4">
                      <div class="font-weight-normal">
                        <strong>{{ comment.username }}</strong> -- Date: {{ formatDate(comment.timestamp) }}
                      </div>
                      <div>{{ comment.text }}</div>
                    </div>
                    <v-btn v-if="comment.username == username" icon size="small" @click="deleteComment(comment)">
                      <v-icon>mdi-delete</v-icon>
                    </v-btn>
                  </div>

                </v-timeline-item>
              </v-timeline>
            </v-card-text>
            
            <!-- <v-text-field v-model="message" label="Add Comment" prepend-icon="mdi-message" class="ml-8 mr-12"></v-text-field>
            <v-btn @click="uploadFile">Upload</v-btn> -->
             <v-row >
              <v-col cols="8" class="pl-10 pr-0">
                <v-text-field v-model="message" label="Add Comment" prepend-icon="mdi-message" ></v-text-field>
              </v-col>
              <v-col cols="4">
                <v-btn @click="uploadFile" color="primary" height="56">Upload</v-btn>
              </v-col>
            </v-row>
          </v-card>
          
          <v-card
          :key="post.id"
          border
          class="mb-4 mt-1 mx-2"
          density="compact"
          title="Tank Details"
          variant="text"
          style="background-color:white;"
          max-width="800"
        >

          <v-card-text class="overflow-y-auto ml-8 pa-0" style="height:200px;">
            <v-simple-table >
              <tbody>
                <tr>
                  <td><strong>Ref:</strong></td>
                  <td>1323</td>
                </tr>
                <tr>
                  <td><strong>Country:</strong></td>
                  <td>Guatemala</td>
                </tr>
                <tr>
                  <td><strong>Size:</strong></td>
                  <td>23</td>
                </tr>
                <tr>
                  <td><strong>Weight:</strong></td>
                  <td>88</td>
                </tr>
                <tr>
                  <td><strong>Client:</strong></td>
                  <td>Mali Losinj</td>
                </tr>
                <tr>
                  <td><strong>Client country:</strong></td>
                  <td>Russia</td>
                </tr>
                <tr>
                  <td><strong>Delivery:</strong></td>
                  <td>21/12/2025</td>
                </tr>
                <tr>
                  <td><strong>Delivery Company:</strong></td>
                  <td>Meverick</td>
                </tr>
                <tr>
                  <td><strong>Delivery Type:</strong></td>
                  <td>Trucks</td>
                </tr>
                <tr>
                  <td><strong>Location of Delivery:</strong></td>
                  <td>Somalia</td>
                </tr>
                <tr>
                  <td><strong>Contact:</strong></td>
                  <td>234 234 324234</td>
                </tr>
                <tr>
                  <td><strong>Email:</strong></td>
                  <td>tank@tank.com</td>
                </tr>
              </tbody>
            </v-simple-table>
          </v-card-text>
        </v-card>
          
          <template v-slot:actions>
            <v-btn color="primary" variant="text">See in Map</v-btn>
          </template>
        </v-card>
      </v-row>               
    </v-card>      
  </v-container>
</v-main>
</template>

<script>
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';
import { mapState } from 'pinia'
export default {
  data() {
    return{
      post:{},
      comments:[],
      file: null,
      message:'',
      username:null
    }
  },
  methods:{
    async deleteComment(comment){
      
      console.log(localStorage.getItem('access_token'))
      axios.post(this.BASE_URL + 'comment/delete/' + comment.id, '',
      {
        headers: {
          'Authorization':'Bearer ' + localStorage.getItem('access_token'),
          'Accept': 'application/json'
        }
      })
        .then(response => {
          console.log(response.data);
          window.location.reload();

        })
        .catch(error => {
          console.error(error);
        });
    },
    async uploadFile() {
      let data = {
        "text": this.message,
        "username": 'matija@gmail.com',
        "post_id": this.post.id
      }
      console.log(data)

      await axios.post(this.BASE_URL + 'comment', data,
      {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      })
        .then(response => {
          console.log(response.data);
          window.location.reload();

        })
        .catch(error => {
          console.error(error);
        });
    },
    formatDate(timestamp) {
      const dateObj = new Date(timestamp);
      const year = dateObj.getFullYear();
      const month = dateObj.getMonth() + 1;
      const date = dateObj.getDate();
      const hours = dateObj.getHours();
      const minutes = dateObj.getMinutes();
      const seconds = dateObj.getSeconds();
      return `${year}-${month}-${date} ${hours}:${minutes}:${seconds}`;
    }
  },
  computed:{
    ...mapState(useCounterStore, ['BASE_URL', 'setUsername'])
  },
  async created(){
      this.username=localStorage.getItem('username')
    
      const url = window.location.href;
      const parts = url.split('/');
      const id = parts.pop()

      await axios.get(this.BASE_URL + 'post/' + id)
      .then(response => {
        console.log('this is post.', response);
        
        this.post = response.data  
        this.post.caption = this.post.caption.toUpperCase()  
      })
      .catch(error => {
        console.error('There was an error:', error.response.data);
      });


      await axios.get(this.BASE_URL + 'comment/all/' + id)
      .then(response => {
        console.log('this is comments.', response);
        
        this.comments = response.data  
      })
      .catch(error => {
        console.error('There was an error:', error.response.data);
      });
  }
}
</script>

<style scoped>

</style>