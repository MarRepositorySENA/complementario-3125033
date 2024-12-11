```
//ENTIDAD USUARIO
@Entity
@Table(name = "usuario")
public class Usuario extends BaseEntity {

	@Column(name = "usuario_nombre", length = 40)
	private String usuarioNombre;

	@Column(name = "contrasenia")
	private String contrasenia;

	@OneToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "persona_id", nullable = false)
	private Persona personaId;

	

	public String getUsuarioName() {
		return usuarioNombre;
	}

	public void setUsuarioName(String usuarioName) {
		this.usuarioNombre = usuarioName;
	}

	public String getContrasenia() {
		return contrasenia;
	}

	public void setContrasenia(String contrasenia) {
		this.contrasenia = contrasenia;
	}

	public Persona getPersonaId() {
		return personaId;
	}

	public void setPersonaId(Persona personaId) {
		this.personaId = personaId;
	}
//IREPOSITORIO USUARIO

@Repository
public interface IUsuarioRepository extends IBaseRepository<Usuario, Long>{
	
	@Query(value = "select  "
			+ "p.primer_nombre, "
			+ "p.segundo_nombre, "
			+ "p.tipo_documento, "
			+ "p.numero_documento, "
			+ "p.telefono, "
			+ "p.email, "
			+ "u.usuario "
			+ "from  "
			+ "persona as p "
			+ "inner join usuario as u on p.id=u.persona_id "
			+ "where u.id = :id", nativeQuery=true)
			Optional<IDatosUsuarioDto> ObtenerDatosUsuario(Long id);
	
	@Query(value = "SELECT    "
			+ "			    u.id as userId,    "
			+ "			    u.state,  "
			+ "             u.contrasenia,  "
			+ "			    u.usuario_nombre,    "
			+ "			    COUNT(usuario_nombre) AS quantity    "
			+ "			 FROM    "
			+ "			    usuario u    "
			+ "			 WHERE    "
			+ "			    u.usuario_nombre = :user AND u.state = TRUE   "
			+ "			 GROUP BY  u.id, u.state, u.usuario_nombre ",nativeQuery = true)
	Optional<ILoginDto> getLogin(String user);
	
	@Query(value = "SELECT    "
			+ "					v.ruta vistaRuta,   "
			+ "					v.nombre vistaNombre,   "
			+ "					mo.ruta moduloRuta,   "
			+ "					mo.nombre moduloNombre,  "
			+ "					mo.icono,  "
			+ "					r.nombre as rol, "
			+ "					CONCAT(pe.primer_nombre, pe.segundo_nombre) as personaNombre  "
			+ "					mo.padre_id    "
			+ "				FROM  persona pe  "
			+ "					INNER JOIN usuario u ON pe.id = u.persona_id   "
			+ "                 INNER JOIN usuarios_roles ur ON u.id = ur.usuario_id "
			+ "					INNER JOIN role r ON r.id = ur.role_id   "
			+ "					INNER JOIN vistas_roles vr ON vr.role_id = r.id   "
			+ "					INNER JOIN vista v ON v.id = vr.vista_id   "
			+ "					INNER JOIN modulo mo ON mo.id = v.modulo_id  "
			+ "				WHERE    "
			+ "					u.usuario_nombre = :user "
			+ "					AND u.state = TRUE   "
			+ "					AND r.state = TRUE   "
			+ "					AND v.state = TRUE   "
			+ "					AND mo.state = TRUE ", nativeQuery = true)
	List<PermisosDto> validarPermisos(String user);

	Optional<Usuario> findByUsuarioNombre(String usuario);

	@Query(value = "select * from usuario " +
			"inner join persona on usuario.persona_id = persona.id " +
			"where persona.email = :email", nativeQuery = true)
	Optional<Usuario> findByEmail(String email);
}
//ISERVICE USUARIO 

package com.persona.Backend.IService.Security;


import java.util.List;
import java.util.Optional;

import com.persona.Backend.Dto.IDatosUsuarioDto;
import com.persona.Backend.Dto.Security.PermisosDto;
import com.persona.Backend.Entity.Security.Usuario;
import com.persona.Backend.IService.IBaseService;

public interface IUsuarioService extends IBaseService<Usuario>{
	
	Optional<IDatosUsuarioDto> ObtenerDatosUsuario(Long id);
	
	Boolean getLogin(String user, String password) throws Exception;
	
	List<PermisosDto> validarPermisos(String user);

	Usuario saveUsuarioJwt(Usuario usuario) throws Exception;

}
 
//SERVICE USUARIO

package com.persona.Backend.Service.Security;

import java.util.List;
import java.util.Optional;

import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import com.persona.Backend.Dto.IDatosUsuarioDto;
import com.persona.Backend.Dto.ILoginDto;
import com.persona.Backend.Dto.Security.PermisosDto;
import com.persona.Backend.Entity.Security.Usuario;
import com.persona.Backend.IRepository.Security.IUsuarioRepository;
import com.persona.Backend.IService.Security.IUsuarioService;
import com.persona.Backend.Service.BaseService;

@Service
public class UsuarioService extends BaseService<Usuario> implements IUsuarioService {

	@Autowired
	private IUsuarioRepository repository;

	private final BCryptPasswordEncoder passwordEncoder;

	public UsuarioService() {
		this.passwordEncoder = new BCryptPasswordEncoder();
	}

	@Override
	public Optional<IDatosUsuarioDto> ObtenerDatosUsuario(Long id) {
		return repository.ObtenerDatosUsuario(id);
	}

	
	@Override
	public Boolean getLogin(String user, String password) throws Exception {
	    Optional<ILoginDto> datosUsuario = repository.getLogin(user);
	    
	    // Verificar si el Optional tiene un valor presente
	    if (datosUsuario.isPresent()) {
	        // Validar usuario y contraseña
	        if (user.equals(datosUsuario.get().getUsuarioNombre()) &&
	            password.equals(datosUsuario.get().getContrasenia())) {
	            return true;
	        } else if (!password.equals(datosUsuario.get().getContrasenia())) {
	            throw new Exception("La contraseña es incorrecta");
	        }
	    } else {
	        // Lanzar excepción si no se encuentra el usuario
	        throw new Exception("Usuario no encontrado");
	    }
	    
	    return false;
	}

	@Override
	public List<PermisosDto> validarPermisos(String user) {
		return repository.validarPermisos(user);
	}

	@Override
	public Usuario saveUsuarioJwt(Usuario usuario) throws Exception {
		String encodedPassword = passwordEncoder.encode(usuario.getContrasenia());
		usuario.setContrasenia(encodedPassword);
		return repository.save(usuario);
	}

	@Transactional
	public String actualizarContrasenia(String email, String nuevaContrasenia) throws Exception {
		Optional<Usuario> usuarioOptional = repository.findByEmail(email);

		if (usuarioOptional.isPresent()) {
			Usuario usuario = usuarioOptional.get();
			String encodedPassword = passwordEncoder.encode(nuevaContrasenia);
			usuario.setContrasenia(encodedPassword);
			repository.save(usuario);
			return "Contraseña actualizada exitosamente.";
		} else {
			throw new Exception("Usuario no encontrado.");
		}
	}

}

//CONTROLLER USUARIO 
package com.persona.Backend.Controller.Security;

import java.util.Optional;
import java.util.List;

import jakarta.mail.MessagingException;
import jakarta.mail.internet.MimeMessage;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.web.bind.annotation.*;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Dto.IDatosUsuarioDto;
import com.persona.Backend.Dto.Security.PermisosDto;
import com.persona.Backend.Entity.Security.Usuario;
import com.persona.Backend.Service.Security.UsuarioService;
import org.thymeleaf.spring6.SpringTemplateEngine;
import org.thymeleaf.context.Context;



@CrossOrigin("*")//permite que cualquier dominio tenga acceso a el
@RestController
@RequestMapping("/api/v1/base/security/usuario")
public class UsuarioController extends BaseController<Usuario> {

	@Autowired
	private UsuarioService service;

	@Autowired
	private JavaMailSender mailSender;

	@Autowired
	private SpringTemplateEngine templateEngine;

	@GetMapping("/datos/usuario/{id}")
	Optional<IDatosUsuarioDto> ObtenerDatosUsuario(@PathVariable Long id){
		return service.ObtenerDatosUsuario(id);
	}

	
	@GetMapping("/validar/datos")
	public Boolean getLogin(@RequestParam String user, String password) throws Exception{
		return service.getLogin(user, password);
	}
	  
	@GetMapping("/validar/permisos")
	public List<PermisosDto> validarPermisos(@RequestParam String User){
		return service.validarPermisos(User);
	}

	@PostMapping("/GuardarUsuarioJwt")
	public Usuario saveUsuarioJwt(@RequestBody Usuario usuario) throws Exception{
		return service.saveUsuarioJwt(usuario);
	}

	@PostMapping("/send-password-reset/{email}")
	public ResponseEntity<String> enviarEmail(@PathVariable String email) {
		try {
			sendPasswordResetEmail(email);
			return ResponseEntity.ok("Correo de recuperación enviado.");
		} catch (MessagingException e) {
			return ResponseEntity.status(500).body("Error al enviar el correo.");
		}
	}

	@PutMapping("/actualizar-contrasenia/{email}")
	public String actualizarContrasenia(@PathVariable String email, @RequestParam String contrasenia) throws Exception {
		System.out.println("Email: " + email + ", Contraseña: " + contrasenia);
		return service.actualizarContrasenia(email, contrasenia);
	}

	public void sendPasswordResetEmail(String userEmail) throws MessagingException {
		String userName = "string";
		MimeMessage message = mailSender.createMimeMessage();
		MimeMessageHelper helper = new MimeMessageHelper(message, true);

		helper.setTo(userEmail);
		helper.setSubject("Restablecimiento de contraseña");

		Context context = new Context();
		context.setVariable("userName", userName);
		context.setVariable("email", userEmail); // Agregar el email al contexto

		String htmlContent = templateEngine.process("RecuperarContrasenia.html", context);
		helper.setText(htmlContent, true);

		mailSender.send(message);
	}


}



```